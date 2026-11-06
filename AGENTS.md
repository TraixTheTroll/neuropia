# Agent guidelines for Neuropia

This repository is the Neuropia research group's website, adapted from al-folio. Its public URL is `https://neuropia.no`, with an empty `baseurl`. Local Jekyll previews use `http://localhost:4000/`. Read the [README](README.md) and [maintenance guide](docs/NEUROPIA.md) before editing.

## Maintained source

- Public pages and biographies: `_pages/`.
- Members, roles, photo paths, thumbnail crops, and links: `_data/members.yml`.
- Group affiliations: `_data/affiliations.yml`.
- Selected publications: `_bibliography/neuropia.bib`.
- Publication review configuration: `_data/publication_sync.yml`; provenance: `sources/`.
- Site-owned templates: `_layouts/neuropia*.liquid` and `_includes/neuropia-*.liquid`.
- Styling and animation: `assets/css/neuropia.css` and `assets/js/neuropia.js`.
- Photos and thumbnails: `assets/img/people/`; thumbnail generator: `bin/generate_people_thumbnails.rb`.

Preserve the approved visual system, always-open main homepage sections, native scrolling, accessible publication-year toggles, member profiles, reduced-motion behavior, scientific qualifications, current photos, and original logo source. The source PNG, deployed lossless WebP, and favicon have separate roles; see the maintenance guide.

The namespaced templates and custom CSS/JavaScript are intentional user-site customizations. They do not shadow installed gem files. Gem-owned runtime changes belong in the owning plugin; see [architecture](docs/ARCHITECTURE.md) and [ownership boundaries](docs/BOUNDARIES.md).

## Build and verification

Use the shared `.ruby-version` and `.node-version` files and the committed lockfiles. Follow the [README validation sequence](README.md#local-preview-and-checks): Prettier, production Jekyll/PurgeCSS build, static site checks, Chromium/WebKit browser checks, and upgrade/override audits. Site checks are in `bin/check_site.rb` and `test/site/`.

The upstream `lint:style-contract`, `test/integration_*.sh`, `test/visual/`, Docker helpers, and their old workflows were removed because they checked the starter rather than this site. Do not run them or use the upstream `/al-folio` example base URL. Other inherited guides are reference material, not the current build procedure.

Keep plugin dependencies in `Gemfile` aligned with activation in `_config.yml`. Preserve the required `al_folio` configuration contract while retaining the core gem, even though Neuropia uses its own visual design. Do not modify generated `_site/`, installed gems, or `gh-pages` to make source changes.

## Publishing and publication review

Changes merged into `main` run the gated publishing workflow. It builds and checks the site before updating `gh-pages`; GitHub Pages then activates that branch. Keep `CNAME` set to `neuropia.no`, use `relative_url` for internal paths, and verify both deployment stages.

Preserve the ORCID discovery workflow and its human review gate. Publication proposals must not be merged automatically. See [publication synchronization](docs/PUBLICATION_SYNC.md).

Keep documentation aligned with the actual site, link to the maintained source of each procedure, and retain the MIT license and upstream attribution.
