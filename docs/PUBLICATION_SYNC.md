# Publication synchronization

The **Sync ORCID publications** workflow checks configured members daily at **05:23 UTC** and proposes new journal articles in a single review pull request. It does not automatically publish or merge them. Accepted additions reach the public Publications page when a maintainer merges the PR into `main` and the normal deployment completes.

## Coverage and data sources

ORCID identifiers live in `_data/members.yml`. Five members are configured initially: Christopher Elnan Kvistad, Torbjørn Kråkenes, Marie Ytterdal, Casper Eugen Sandvik, and Lars Bø. Their identity checks are recorded in [`sources/orcid-sync/README.md`](../sources/orcid-sync/README.md).

Andrea Gremes, Christian Grønås, and Anna-Maria Rasmussen Eitrheim are not monitored until verified ORCID identifiers are added. Add each person's bare, hyphenated identifier to their existing member entry. The next scan includes them automatically. Each run's summary lists monitored members and missing identifiers.

The importer reads public journal-article work summaries from the [ORCID Public API](https://info.orcid.org/what-is-orcid/services/public-api/) and retrieves bibliographic metadata from the [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). It checks the work's own DOI, not identifiers for a journal or related work. DOIs are normalized before comparing against existing entries and other members' records. Shared papers are proposed only once.

Only records available publicly in ORCID can be discovered. Records can lag publication or be incomplete. [Crossref/DataCite auto-updates](https://info.orcid.org/small-publishers-faq/) can help keep researchers' ORCID records current when the authors authorize them. Journal articles without a DOI, or without usable Crossref metadata, need manual entry; the run summary reports metadata problems. Books, preprints, datasets, and other work types are not imported.

Public API requests work without an ORCID secret in the initial setup. An optional `ORCID_ACCESS_TOKEN` repository secret can provide a `/read-public` token if needed later. It is sent only to ORCID, never Crossref, and is not saved to publication data. No researcher passwords or access to private records are needed.

## Review and accept proposals

The automation maintains the branch `automation/orcid-publications` and one PR titled **Publications: review new ORCID articles**. If no new articles are found, no new PR is opened. Each proposal lists titles, DOI links, matched researchers, coverage, and any metadata problems.

1. Check that each paper belongs in Neuropia's selected bibliography. A member's ORCID can include research outside the group's focus.
2. Check author names, publication year, journal, and DOI. Existing hand-curated entries and custom labels are never rewritten by the importer.
3. Merge the PR to accept the proposed articles. Wait for **Deploy site** and **pages-build-deployment** before checking the website.

The bot regenerates its proposal from `main` and public metadata on each run. Do not rely on manual edits to the automation branch surviving. For a lasting correction, add or edit the entry on `main`; its DOI then prevents duplicate import. You can copy only the desired entries from a mixed proposal into a normal content PR, merge those, and let the next scan regenerate the remainder.

To reject a paper permanently, add its DOI to `excluded_dois` in `_data/publication_sync.yml` through a normal content PR. After that change is merged, the next scan removes it from the proposal. Closing the proposal alone does not record a rejection, so a later scan can reopen it.

The initial publication cutoff is **1 January 2026**, configured as `since` in `_data/publication_sync.yml`. This avoids importing a large historical bibliography. Metadata dates before that cutoff or in the future are omitted. When online and print dates differ, the earliest published date is used. Missing months or days are treated as January or the first of the month, respectively.

## Run manually

On GitHub, open **Actions → Sync ORCID publications → Run workflow**, select `main`, and run it. Enable **dry_run** to generate only a summary without modifying the bibliography or opening a PR. The **sync** job summary contains the report, including coverage when no additions are found.

The schedule and manual runs operate only on `main`. Pull requests touching the importer or its inputs run the network-free tests without write permissions. Normal GitHub PR checks are not triggered by PRs created with `GITHUB_TOKEN`; the sync job therefore builds proposed additions with Jekyll before creating or updating their PR. A maintainer's merge triggers the normal deployment.

GitHub's **Allow GitHub Actions to create and approve pull requests** setting must be enabled for PR creation. The workflow requests only repository contents and pull-request write permissions and never approves a PR or enables automatic merging. It uses GitHub's built-in token, so no personal access token is required. As with other scheduled Actions, GitHub can delay runs or disable scheduling on inactive public repositories; inspect Actions if expected scans stop.

## Local checks

From the repository root, create a dedicated environment and install the pinned dependencies:

```bash
python3 -m venv .venv-publications
.venv-publications/bin/python -m pip install -r requirements-publications.txt
.venv-publications/bin/python -m unittest discover -s test -p 'test_orcid_publications.py' -v
.venv-publications/bin/python bin/sync_orcid_publications.py --dry-run
```

Run without `--dry-run` to append proposed entries locally. `--report /path/to/report.md` saves the review report. The importer validates the complete candidate bibliography before writing. An ORCID/API outage fails the scan before any publication additions are written; missing or invalid Crossref metadata is reported without removing existing entries.

After actual additions, format the generated provenance and build the site:

```bash
npx prettier sources/orcid-sync/imports.json --write
npm run lint:prettier
JEKYLL_ENV=production bundle exec jekyll build
```

The implementation is in `bin/sync_orcid_publications.py`, its configuration in `_data/publication_sync.yml`, and its regression tests in `test/test_orcid_publications.py`. Source records and provenance are excluded from the public site. The original `_bibliography/neuropia.bib` remains the single bibliography used by the website.
