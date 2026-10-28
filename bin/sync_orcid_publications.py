#!/usr/bin/env python3
"""Propose public ORCID journal articles without rewriting curated BibTeX."""

import argparse
from datetime import date
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen

import bibtexparser
import yaml


class SyncError(Exception):
    """The scan cannot safely complete."""


def normalize_doi(value):
    value = unquote(str(value or "").strip())
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value, flags=re.I)
    if not re.fullmatch(r'10\.\d{4,9}/[^\s{}<>"\\]+', value):
        raise ValueError(f"Invalid DOI: {value!r}")
    return value.lower()


def validate_orcid(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", value):
        raise SyncError(f"Invalid ORCID: {value!r}")
    digits = value.replace("-", "")
    total = 0
    for digit in digits[:-1]:
        total = (total + int(digit)) * 2
    check = (12 - total % 11) % 11
    if digits[-1] != ("X" if check == 10 else str(check)):
        raise SyncError(f"Invalid ORCID checksum: {value}")
    return value


def fetch_json(url):
    headers = {
        "Accept": "application/json",
        "User-Agent": "Neuropia-publication-sync/1.0 (https://github.com/TraixTheTroll/neuropia)",
    }
    token = os.environ.get("ORCID_ACCESS_TOKEN")
    if token and url.startswith("https://pub.orcid.org/"):
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers=headers), timeout=30) as response:
                return json.load(response)
        except HTTPError as exc:
            if exc.code == 404:
                return None
            if exc.code != 429 and exc.code < 500:
                raise SyncError(f"HTTP {exc.code} fetching {url}") from exc
            reason = f"HTTP {exc.code}"
        except (URLError, TimeoutError, OSError) as exc:
            reason = type(exc).__name__
        except (ValueError, UnicodeError) as exc:
            raise SyncError(f"Invalid JSON from {url}") from exc
        if attempt < 2:
            time.sleep(2 ** attempt)
    raise SyncError(f"{reason} fetching {url} after three attempts")


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, text):
        self.parts.append(text)


def plain(value):
    parser = PlainText()
    parser.feed(str(value or ""))
    return " ".join(unescape("".join(parser.parts)).split())


def tex(value):
    """Escape plain text once; do not reinterpret decoded text as HTML."""
    replacements = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
        "<": r"\textless{}", ">": r"\textgreater{}",
    }
    return "".join(replacements.get(c, c) for c in str(value))


def read_bibliography(text):
    library = bibtexparser.parse_string(text)
    if library.failed_blocks:
        raise SyncError("Bibliography contains unparseable blocks; no changes written")
    dois = set()
    keys = set()
    for entry in library.entries:
        if entry.key in keys:
            raise SyncError(f"Duplicate bibliography key: {entry.key}")
        keys.add(entry.key)
        if "doi" in entry.fields_dict:
            dois.add(normalize_doi(entry.fields_dict["doi"].value))
    return dois, keys


def work_dois(group, since):
    """Use only a work's own DOI, never its journal/related-work identifiers."""
    found = set()
    summaries = group.get("work-summary")
    if not isinstance(summaries, list):
        raise SyncError("Invalid ORCID work summaries")
    for work in summaries:
        if work.get("type") != "journal-article" or work.get("visibility") != "public":
            continue
        year = ((work.get("publication-date") or {}).get("year") or {}).get("value")
        if year and int(year) < since.year:
            continue
        identifiers = work.get("external-ids") or group.get("external-ids") or {}
        for external in identifiers.get("external-id", []):
            if external.get("external-id-type", "").lower() != "doi":
                continue
            if external.get("external-id-relationship") != "self":
                continue
            try:
                found.add(normalize_doi(external.get("external-id-value")))
            except ValueError:
                continue
    return found


def publication_date(metadata):
    dates = []
    for key in ["published-online", "published-print", "published", "issued"]:
        parts = (metadata.get(key) or {}).get("date-parts", [])
        if parts and parts[0]:
            values = parts[0]
            dates.append(date(int(values[0]), int(values[1]) if len(values) > 1 else 1,
                              int(values[2]) if len(values) > 2 else 1))
    if not dates:
        raise ValueError("no publication date")
    return min(dates)


def make_entry(doi, metadata, since, today):
    if not isinstance(metadata, dict):
        raise ValueError("invalid Crossref record")
    if normalize_doi(metadata.get("DOI")) != doi:
        raise ValueError("Crossref returned a different DOI")
    if metadata.get("type") != "journal-article":
        return None
    published = publication_date(metadata)
    if not since <= published <= today:
        return None
    title = plain((metadata.get("title") or [""])[0])
    journal = plain((metadata.get("container-title") or [""])[0])
    authors = []
    for author in metadata.get("author", []):
        family, given = plain(author.get("family")), plain(author.get("given"))
        if family:
            authors.append(tex(family) + (", " + tex(given) if given else ""))
        elif author.get("name"):
            authors.append("{" + tex(plain(author["name"])) + "}")
        else:
            raise ValueError("incomplete author name")
    if not title or not journal or not authors:
        raise ValueError("missing title, journal, or authors")
    key = "orcid_" + hashlib.sha256(doi.encode()).hexdigest()[:16]
    fields = [
        ("title", "{" + tex(title) + "}"),
        ("author", " and ".join(authors)),
        ("journal", tex(journal)),
        ("year", str(published.year)),
    ]
    for source, target in [("volume", "volume"), ("issue", "number")]:
        if metadata.get(source):
            fields.append((target, tex(plain(metadata[source]))))
    pages = metadata.get("page") or metadata.get("article-number")
    if pages:
        fields.append(("pages", tex(plain(pages))))
    fields.extend([("doi", doi), ("html", "https://doi.org/" + quote(doi, safe="/():;")),
                   ("bibtex_show", "true")])
    entry = "@article{" + key + ",\n"
    entry += ",\n".join("  " + k + " = {" + v + "}" for k, v in fields)
    entry += "\n}\n"
    return {"key": key, "doi": doi, "title": title, "year": published.year, "bibtex": entry}


def synchronize(root, get=fetch_json, today=None, dry_run=False):
    today = today or date.today()
    config = yaml.safe_load((root / "_data/publication_sync.yml").read_text())
    since = date.fromisoformat(str(config["since"]))
    excluded = {normalize_doi(d) for d in config.get("excluded_dois", [])}
    members = yaml.safe_load((root / "_data/members.yml").read_text())
    bibliography = root / "_bibliography/neuropia.bib"
    original = bibliography.read_text()
    existing, keys = read_bibliography(original)
    provenance_path = root / "sources/orcid-sync/imports.json"
    provenance = json.loads(provenance_path.read_text())
    candidates = {}
    monitored, missing = [], []
    ids = set()
    for member in members:
        if not member.get("orcid"):
            missing.append(member["name"])
            continue
        orcid = validate_orcid(member["orcid"])
        if orcid in ids:
            raise SyncError(f"ORCID assigned to multiple members: {orcid}")
        ids.add(orcid)
        person = {"name": member["name"], "orcid": orcid}
        monitored.append(person)
        record = get(f"https://pub.orcid.org/v3.0/{orcid}/works")
        if not isinstance(record, dict) or not isinstance(record.get("group"), list):
            raise SyncError(f"Cannot read public works for {member['name']} ({orcid})")
        for group in record["group"]:
            for doi in work_dois(group, since) - existing - excluded:
                candidates.setdefault(doi, {})[orcid] = person
    if not monitored:
        raise SyncError("No members have an ORCID; no scan was performed")
    added, warnings = [], []
    for doi in sorted(candidates):
        url = "https://api.crossref.org/works/" + quote(doi, safe="")
        response = get(url)
        if response is None:
            warnings.append(f"No Crossref metadata for {doi}; left for a later scan")
            continue
        try:
            entry = make_entry(doi, response["message"], since, today)
        except (ValueError, KeyError, TypeError, IndexError) as exc:
            warnings.append(f"Skipped {doi}: {exc}")
            continue
        if entry is None:
            continue
        if entry["key"] in keys:
            raise SyncError(f"Citation key collision: {entry['key']}")
        keys.add(entry["key"])
        entry["members"] = sorted(candidates[doi].values(), key=lambda m: m["name"])
        entry["metadata_source"] = url
        added.append(entry)
    if added:
        separator = "\n" if original.endswith("\n") else "\n\n"
        updated = original + separator + "\n".join(e["bibtex"] for e in added)
        # Validate the complete candidate file before changing either tracked file.
        read_bibliography(updated)
        provenance.extend({k: v for k, v in e.items() if k not in ["bibtex", "key"]} for e in added)
        if not dry_run:
            bibliography.write_text(updated)
            provenance_path.write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    return {"added": added, "monitored": monitored, "missing": missing, "warnings": warnings,
            "since": since.isoformat(), "dry_run": dry_run}


def markdown_text(value):
    return re.sub(r"([\\`*_{}\[\]()<>|])", r"\\\1", plain(value))


def review_report(result):
    lines = ["## ORCID publication scan", "",
             f"Proposed articles: **{len(result['added'])}**. Publication cutoff: **{result['since']}**.", "",
             "These are candidates from public ORCID records, with bibliographic metadata from Crossref.",
             "Review relevance to Neuropia, author names, dates, and metadata before merging.",
             "Existing curated entries are preserved. Merging publishes the additions through the normal site deployment.", ""]
    for entry in result["added"]:
        lines.append(f"- **{markdown_text(entry['title'])}** ({entry['year']}) — "
                     f"[DOI](https://doi.org/{quote(entry['doi'], safe='/():;')})")
        matches = ", ".join(f"[{markdown_text(m['name'])}](https://orcid.org/{m['orcid']})" for m in entry["members"])
        lines.append(f"  Matched members: {matches}.")
    lines.extend(["", "### Coverage", ""])
    for member in result["monitored"]:
        lines.append(f"- [{markdown_text(member['name'])}](https://orcid.org/{member['orcid']})")
    if result["missing"]:
        lines.extend(["", "Not monitored yet (no ORCID configured): " + ", ".join(result["missing"]) + "."])
    if result["warnings"]:
        lines.extend(["", "### Items needing attention", ""])
        lines.extend("- " + markdown_text(w) for w in result["warnings"])
    lines.extend(["", "To reject a DOI permanently, add it to `excluded_dois` in `_data/publication_sync.yml`.",
                  "The automation regenerates this proposal; make lasting corrections on main.",
                  "See [the sync guide](https://github.com/TraixTheTroll/neuropia/blob/main/docs/PUBLICATION_SYNC.md).", ""])
    if result["dry_run"]:
        lines.append("Dry run: no bibliography or provenance changes were written.\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        result = synchronize(args.root, dry_run=args.dry_run)
    except (SyncError, ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"ORCID sync failed: {exc}\n")
    report = review_report(result)
    if args.report:
        args.report.write_text(report)
    print(report)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"added={len(result['added'])}\n")


if __name__ == "__main__":
    main()
