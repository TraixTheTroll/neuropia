"""Network-free regression tests for publication discovery and safe appends."""

from datetime import date
import io
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import yaml

SPEC = importlib.util.spec_from_file_location("orcid_sync", Path(__file__).parents[1] / "bin/sync_orcid_publications.py")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)

DOI = "10.5555/neuropia-test"
ORCID = "0009-0002-5931-7670"
SECOND_ORCID = "0009-0004-6032-7600"
TODAY = date(2026, 10, 28)


def work(doi=DOI, year="2026", kind="journal-article", relationship="self"):
    return {"work-summary": [{
        "type": kind, "visibility": "public",
        "publication-date": {"year": {"value": year}},
        "external-ids": {"external-id": [{"external-id-type": "doi",
                                            "external-id-value": doi,
                                            "external-id-relationship": relationship}]},
    }]}


def metadata(doi=DOI):
    return {"message": {
        "DOI": doi, "type": "journal-article",
        "title": ["A <i>test</i> of cells & vesicles: {RNA}_100%"],
        "container-title": ["Test Journal"],
        "author": [{"family": "Kråkenes", "given": "Torbjørn"}, {"name": "Test Consortium"}],
        "published-online": {"date-parts": [[2026, 4, 20]]},
        "published-print": {"date-parts": [[2027, 1]]},
        "volume": "1", "issue": "2", "article-number": "e123",
    }}


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for d in ["_data", "_bibliography", "sources/orcid-sync"]:
            (self.root / d).mkdir(parents=True)
        self.bib = self.root / "_bibliography/neuropia.bib"
        self.original = "% Curated note retained exactly.\n@article{manual, title={{Original}}, author={Smith, A}, year={2024}, doi={10.5555/original}}\n\n"
        self.bib.write_text(self.original)
        (self.root / "sources/orcid-sync/imports.json").write_text("[]\n")
        self.members = [{"name": "Casper", "orcid": ORCID}, {"name": "Marie", "orcid": SECOND_ORCID}, {"name": "Missing ID"}]
        self.configure()

    def configure(self, excluded=None):
        (self.root / "_data/members.yml").write_text(yaml.safe_dump(self.members))
        (self.root / "_data/publication_sync.yml").write_text(yaml.safe_dump({"since": "2026-01-01", "excluded_dois": excluded or []}))

    def get(self, url):
        if "pub.orcid.org" in url:
            return {"group": [work(), work("https://doi.org/10.5555/NEUROPIA-TEST")]}
        return metadata()

    def test_shared_paper_appended_once_and_second_run_is_noop(self):
        result = sync.synchronize(self.root, self.get, TODAY)
        self.assertEqual(len(result["added"]), 1)
        self.assertEqual(len(result["added"][0]["members"]), 2)
        self.assertEqual(result["missing"], ["Missing ID"])
        updated = self.bib.read_text()
        self.assertTrue(updated.startswith(self.original))
        dois, keys = sync.read_bibliography(updated)
        self.assertEqual(dois, {"10.5555/original", DOI})
        self.assertEqual(len(keys), 2)
        self.assertIn(r"\&", updated)
        self.assertIn(r"\{RNA\}\_100\%", updated)
        self.assertNotIn("<i>", updated)
        provenance = (self.root / "sources/orcid-sync/imports.json").read_bytes()
        self.assertEqual(len(sync.synchronize(self.root, self.get, TODAY)["added"]), 0)
        self.assertEqual(self.bib.read_text(), updated)
        self.assertEqual((self.root / "sources/orcid-sync/imports.json").read_bytes(), provenance)

    def test_dry_run_does_not_write(self):
        result = sync.synchronize(self.root, self.get, TODAY, dry_run=True)
        self.assertEqual(len(result["added"]), 1)
        self.assertEqual(self.bib.read_text(), self.original)
        self.assertEqual(json.loads((self.root / "sources/orcid-sync/imports.json").read_text()), [])
        self.assertIn("Dry run", sync.review_report(result))

    def test_excluded_and_existing_dois_do_not_fetch_metadata(self):
        self.configure(["https://doi.org/10.5555/NEUROPIA-TEST"])
        def get(url):
            self.assertIn("pub.orcid.org", url)
            return {"group": [work(), work("doi:10.5555/ORIGINAL")]}
        self.assertEqual(sync.synchronize(self.root, get, TODAY)["added"], [])

    def test_skip_other_work_types_related_ids_private_and_old_work(self):
        groups = [work(kind="preprint"), work(relationship="part-of"), work(year="2025")]
        private = work(); private["work-summary"][0]["visibility"] = "limited"
        groups.append(private)
        for group in groups:
            self.assertEqual(sync.work_dois(group, date(2026, 1, 1)), set())

    def test_dates_use_earliest_publication_and_exclude_future(self):
        m = metadata()["message"]
        entry = sync.make_entry(DOI, m, date(2026, 1, 1), TODAY)
        self.assertEqual(entry["year"], 2026)
        self.assertIsNone(sync.make_entry(DOI, m, date(2026, 5, 1), TODAY))
        m["published-online"]["date-parts"] = [[2027, 2, 1]]
        self.assertIsNone(sync.make_entry(DOI, m, date(2026, 1, 1), TODAY))

    def test_metadata_missing_or_wrong_doi_is_reported_without_writing(self):
        for response in [None, {"message": {}}, metadata("10.5555/wrong")]:
            def get(url):
                return {"group": [work()]} if "pub.orcid.org" in url else response
            result = sync.synchronize(self.root, get, TODAY)
            self.assertTrue(result["warnings"])
            self.assertEqual(self.bib.read_text(), self.original)

    def test_network_failure_after_a_candidate_does_not_write_partial_results(self):
        def get(url):
            if "pub.orcid.org" in url:
                return {"group": [work(), work("10.5555/z-later")]}
            if "z-later" in url:
                raise sync.SyncError("temporary API outage")
            return metadata()
        with self.assertRaises(sync.SyncError):
            sync.synchronize(self.root, get, TODAY)
        self.assertEqual(self.bib.read_text(), self.original)

    def test_bad_orcid_and_duplicate_ids_fail(self):
        for member_list in [[{"name": "Bad", "orcid": "0009-0002-5931-7671"}],
                            [{"name": "A", "orcid": ORCID}, {"name": "B", "orcid": ORCID}]]:
            self.members = member_list; self.configure()
            with self.assertRaises(sync.SyncError):
                sync.synchronize(self.root, self.get, TODAY)

    def test_invalid_bibliography_fails_without_rewriting(self):
        self.bib.write_text("@article{broken, title={unterminated")
        with self.assertRaises(sync.SyncError):
            sync.synchronize(self.root, self.get, TODAY)
        self.assertEqual(self.bib.read_text(), "@article{broken, title={unterminated")

    def test_no_ids_is_not_a_successful_scan(self):
        self.members = [{"name": "No ID"}]; self.configure()
        with self.assertRaises(sync.SyncError):
            sync.synchronize(self.root, self.get, TODAY)

    @patch.object(sync.time, "sleep")
    @patch.object(sync, "urlopen")
    def test_http_rate_limit_and_server_errors_retry(self, open_url, sleep):
        for code in [429, 503]:
            open_url.reset_mock(); sleep.reset_mock()
            open_url.side_effect = HTTPError("https://pub.orcid.org/test", code, "unavailable", {}, None)
            with self.assertRaises(sync.SyncError):
                sync.fetch_json("https://pub.orcid.org/test")
            self.assertEqual(open_url.call_count, 3)
            self.assertEqual(sleep.call_count, 2)

    @patch.dict(sync.os.environ, {"ORCID_ACCESS_TOKEN": "test-only-token"})
    @patch.object(sync, "urlopen")
    def test_optional_token_is_never_sent_to_crossref(self, open_url):
        open_url.side_effect = [io.BytesIO(b"{}"), io.BytesIO(b"{}")]
        sync.fetch_json("https://pub.orcid.org/v3.0/test/works")
        sync.fetch_json("https://api.crossref.org/works/test")
        self.assertEqual(open_url.call_args_list[0].args[0].get_header("Authorization"), "Bearer test-only-token")
        self.assertIsNone(open_url.call_args_list[1].args[0].get_header("Authorization"))

    def test_encoded_html_cannot_become_raw_markup_in_bibtex(self):
        m = metadata()["message"]
        m["title"] = ["&lt;img src=x onerror=alert(1)&gt;"]
        entry = sync.make_entry(DOI, m, date(2026, 1, 1), TODAY)
        self.assertNotIn("<img", entry["bibtex"])
        self.assertIn(r"\textless{}", entry["bibtex"])

    def test_synthetic_candidate_round_trips_through_bibtex_parser(self):
        entry = sync.make_entry(DOI, metadata()["message"], date(2026, 1, 1), TODAY)
        self.assertEqual(sync.read_bibliography(entry["bibtex"])[0], {DOI})
        self.assertIn("{Test Consortium}", entry["bibtex"])


if __name__ == "__main__":
    unittest.main()
