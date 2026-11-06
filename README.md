# Neuropia

This repository contains the public website for **Neuropia**, a research group in Bergen, Norway. It introduces our research, current members, selected publications, and affiliations.

**Website:** [neuropia.no](https://neuropia.no/)

**Repository:** [TraixTheTroll/neuropia](https://github.com/TraixTheTroll/neuropia)

## Research and affiliations

Neuropia investigates mesenchymal stem cells (MSCs) and extracellular vesicles (EVs) as potential therapeutic approaches for neurological disease. Multiple sclerosis is the main disease focus, with broader interests in neurodegenerative disorders, including Parkinson’s disease.

The group is affiliated with:

- Neuro-SysMed, Department of Neurology, Haukeland University Hospital, 5021 Bergen, Norway.
- Department of Clinical Medicine, Faculty of Medicine, University of Bergen, 5021 Bergen, Norway.

Research descriptions distinguish laboratory, animal-model, review, and clinical evidence. Publications are a selected bibliography by current members, including collaborative and historical work; they are not a complete publication list or evidence of established therapeutic benefit.

## Website content

The animated homepage contains **About, Research, People, Publications, and Contact** sections. Navigation scrolls to each section; main sections remain open. Publications are grouped into collapsible year boxes, all open by default. The dark visual design follows the group-supplied `neuropia-main/index.html`, including its floating logo, typography, translucent panels, and particle background. Mobile navigation remains available. Visitors who request reduced motion receive a static background and no animated scrolling. Each member has a clickable profile with a larger image and an editable biography. Christopher’s and Casper’s profiles include biographies and contact details; Torbjørn’s profile introduces his basic research leadership. Other biographies currently contain placeholders.

| Content                                             | Where to edit                                                  |
| --------------------------------------------------- | -------------------------------------------------------------- |
| Homepage                                            | [`_pages/about.md`](_pages/about.md)                           |
| Research themes                                     | [`_pages/research.md`](_pages/research.md)                     |
| Member names, roles, image paths, and profile slugs | [`_data/members.yml`](_data/members.yml)                       |
| People directory                                    | [`_pages/profiles.md`](_pages/profiles.md)                     |
| Individual biographies                              | `_pages/member-<slug>.md`                                      |
| Member images                                       | [`assets/img/people/`](assets/img/people/)                     |
| Selected publications                               | [`_bibliography/neuropia.bib`](_bibliography/neuropia.bib)     |
| Publications page                                   | [`_pages/publications.md`](_pages/publications.md)             |
| Group affiliations                                  | [`_data/affiliations.yml`](_data/affiliations.yml)             |
| Contact page                                        | [`_pages/contact.md`](_pages/contact.md)                       |
| Logo                                                | [`assets/img/neuropia-logo.png`](assets/img/neuropia-logo.png) |
| Group colors and styles                             | [`assets/css/neuropia.css`](assets/css/neuropia.css)           |
| Site settings and enabled features                  | [`_config.yml`](_config.yml)                                   |

The shared page shell is `_layouts/neuropia.liquid`. Homepage and standalone pages share `_includes/neuropia-people.liquid`, `_includes/neuropia-publications.liquid`, and `_includes/neuropia-contact.liquid`; publications render through `_layouts/neuropia-bib.liquid`. Animation code lives in `assets/js/neuropia.js`. Existing `/research/`, `/people/`, `/publications/`, and `/contact/` URLs remain available with the new design.

See [Maintaining the Neuropia website](docs/NEUROPIA.md) for editing details, image handling, branding, and known limitations. [Publication provenance](sources/README.md) records the PubMed search, author checks, and screening decisions; `sources/` is excluded from the published website.

## Local preview and checks

The site is built with Jekyll and pinned Ruby plugin gems. Use Ruby **3.4** and Node.js **24 LTS**, matching `.ruby-version` and `.node-version`. ImageMagick is needed only when regenerating portrait thumbnails. Python is needed only for the separate ORCID publication tools. Dependency versions are recorded in `Gemfile.lock` and `package-lock.json`; the deployment environment is defined in [the workflow](.github/workflows/deploy.yml).

From the repository root:

```bash
bundle install
npm ci
bundle exec jekyll serve
```

Open **http://localhost:4000/**. The custom domain serves the site from its root, with an empty `baseurl`.

For content or styling changes:

```bash
npm run lint:prettier
npm run build
npm run check:site
npx playwright install chromium webkit
npm run test:site
```

If gems are installed locally under `vendor/bundle`, prefix Bundler commands with `BUNDLE_PATH=vendor/bundle`.

## Deployment

Public ORCID journal articles are checked daily and proposed as bibliography additions in a review PR. Merging an accepted proposal publishes it through the normal deployment. See [Publication synchronization](docs/PUBLICATION_SYNC.md) for configuration and review instructions.

The production configuration is:

```yaml
url: https://neuropia.no
baseurl: ""
```

Changes merged into `main` trigger **Deploy site**, which builds `_site`, checks all pages and local links, runs Chromium/WebKit browser checks, and publishes only after those checks pass. It publishes to the `gh-pages` branch. GitHub Pages then publishes that branch. Verify both stages before checking the live site.

Keep the source `CNAME` file set to `neuropia.no`. Use Jekyll’s `relative_url` filter for internal links and assets. Edit source files rather than generated `_site` output or the `gh-pages` branch.

## Notes for maintainers and AI agents

Read [AGENTS.md](AGENTS.md) and [the Neuropia maintenance guide](docs/NEUROPIA.md) before making changes. This repository is a customized research group website. Preserve its group identity, navigation, member profiles, branding, publication provenance, and scientific qualifications.

Some inherited documentation and agent instructions describe the generic starter and use `/al-folio` as an example base URL. For this website, use `_config.yml` and the Neuropia maintenance guide: the correct public URL is **`https://neuropia.no`**, with an empty `baseurl`. Unused example posts, pages, media, bibliographies, plugins and upstream-only workflows have been removed; group publications use `neuropia.bib`.

Keep content edits in the files listed above. Neuropia uses custom layouts and includes for its supplied design while retaining the Jekyll and publication tooling. The inherited `lint:style-contract` checks the upstream starter and intentionally rejects user-site custom layouts; it is not a check for this website. Consult [architecture](docs/ARCHITECTURE.md) and [ownership boundaries](docs/BOUNDARIES.md) before changing them. Plugin changes must keep `Gemfile` and `_config.yml` aligned. The Neuropia templates have distinct names and do not shadow gem-owned files. Run `bundle exec al-folio upgrade overrides audit` when adding or changing layouts.

## Original template and attribution

Neuropia was built from **[al-folio by Maruan Al-Shedivat and contributors](https://github.com/alshedivat/al-folio)**, a Jekyll starter for academic websites. This site uses its **v1.x plugin-based architecture**, with `al_folio_core` currently pinned to **1.0.15**. Check [`Gemfile`](Gemfile) and [`Gemfile.lock`](Gemfile.lock) for the exact installed plugin versions before making upgrades.

The original template is distributed under the **MIT License**; its copyright and license notice are retained in [`LICENSE`](LICENSE). The linked upstream repository is the source template for future agents and maintainers; this repository contains the Neuropia-specific adaptation.
