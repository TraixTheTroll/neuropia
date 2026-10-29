# Maintaining the Neuropia website

The website uses al-folio with group content stored separately from its example content. The homepage follows the supplied `neuropia-main/index.html` design: dark navy, Cormorant Garamond and Inter fonts, teal/gold accents, a floating logo, animated particles, and translucent panels. Navigation scrolls to About, Research, People, Publications, and Contact. Every section stays open; there are no accordion controls. Existing standalone page and member URLs remain available. The prototype is the visual reference; repository content remains the maintained source.

## Members

Edit `_data/members.yml`. Entries appear in file order. Current roles were supplied by the group; individual affiliations are not assigned. Optional fields are `role`, `bio`, `image`, `email`, `orcid`, `linkedin`, and `website`. Store photos under `assets/img/` and set `image` to the filename. Supply the bare ORCID identifier and complete HTTPS URLs for `linkedin` and `website`. Initials appear when no photo is supplied. Current member images are in `assets/img/people/`. Supplied TIFF and PNG files were converted to JPEG at their original pixel dimensions; supplied WebP images are used unchanged. The source images remain unchanged in the supplied folder.

Each member has a stable `slug` and an individual Markdown page at `_pages/member-<slug>.md`, published under `/people/<slug>/`. The People cards link to these pages. Edit the short About section on each page to replace its placeholder with a biography. Images and roles are read from `_data/members.yml`; profile pages preserve each image's full aspect ratio. Profile photos are not clickable and have no full-size-image caption. Directory thumbnails use a circular crop for a consistent grid.

Member profiles use About, optional Research interests, and optional Links sections. Current work and per-person Selected publications sections are omitted. Casper’s page provides the first completed example. Individual profiles display LinkedIn, ORCID, and institutional profile links first, followed by a separate Email line. The full email address remains visible and selectable and links to a `mailto:` target. These details come from `_data/members.yml`; missing details are hidden. The People directory links to each member’s profile without displaying contact or social links.

The People cards use the supplied design’s circular thumbnails and open each full profile. Member pages share the animated shell and show the complete photo at its natural aspect ratio. Typography follows the supplied design, replacing the earlier bold al-folio headings.

## Affiliations

Edit `_data/affiliations.yml`. The homepage and Contact page read the same list. These describe group affiliations, not affiliations assigned to each individual member. Neuro-SysMed’s `url` is used only for its link in the homepage introduction. Names in the Affiliations section remain plain text.

## Publications

New public ORCID journal articles are checked daily and proposed in a review PR. See [Publication synchronization](PUBLICATION_SYNC.md) for coverage, review, exclusions, and manual runs. The automation never merges publication proposals automatically.

Edit `_bibliography/neuropia.bib`. The initial selection contains eight PubMed-verified publications from 2022–2026, with DOI, PubMed, and PMC full-text links. Both the homepage and Publications page render the bibliography in descending year order through `_includes/neuropia-publications.liquid` and `_layouts/neuropia-bib.liquid`. Entries show the first three authors, the remaining author count, journal/year, and DOI, PubMed, and article links when available. The full author lists and metadata remain in the bibliography. The template's `papers.bib` is retained as an example and is not used for group publications. The custom design does not load the old theme’s publication filter, search palette, or light/dark toggle. It uses the supplied dark appearance. See `sources/README.md` for queries, screening decisions, metadata, and editorial limits. The sources directory is excluded from the website build.

## Research and news

Research themes are introduced on the homepage and in `_pages/research.md`. Keep research interests distinct from demonstrated findings, and preserve the links supporting study descriptions. The current page distinguishes clinical, cell-culture, animal-model, and review evidence. Add project descriptions and news when group content is available. Template examples remain in the repository but are excluded from the website through `_config.yml`; remove the relevant exclusions when replacing those examples with real content. External example feeds are disabled.

## Build and deployment

The current project site uses `url: https://traixthetroll.github.io` and `baseurl: /neuropia`. Use `relative_url` for internal links so the project prefix is preserved. Run `bundle exec jekyll build` with the configured base URL. Merging changes into `main` triggers the existing GitHub Pages deployment.

Use `layout: neuropia` on public pages. `_layouts/neuropia.liquid` loads the shared navigation, stylesheet, animation, canonical URL, description, favicon, and footer. Homepage content is in `_pages/about.md`; member pages retain their existing Markdown biographies. Shared People and Contact content is rendered by `_includes/neuropia-people.liquid` and `_includes/neuropia-contact.liquid`.

The namespaced templates do not shadow gem files. Local templates are supported for this user site; the inherited upstream-only `lint:style-contract` is not applicable. Validate changes with Prettier, the production build, relevant regression/browser checks, and the al-folio upgrade and override audits.

`assets/js/neuropia.js` preserves the reference’s particle/star animation and desktop scroll transition. It pauses animation in hidden tabs and honors reduced-motion preferences. Section navigation uses ordinary anchor links with fixed-header offsets, never collapse handlers. The stylesheet and script carry a version query in the shared layout; update it with future changes to avoid stale cached assets.

## Logo and palette

`assets/img/neuropia-logo.png` remains the unchanged group-supplied transparent PNG (3000 × 3000 pixels). It floats above the homepage title and supplies the favicon. The reference palette is dark navy `#050d14`, teal `#2ec4b6`, warm gold `#ff9f1c`, text `#e8e6e3`, and muted text `#a8b2b9`. Shared styling lives in `assets/css/neuropia.css`.

The earlier neuron wallpaper asset remains in the repository at `assets/img/backgrounds/dm-wallpaper.png`, but the new design uses the reference’s animated canvas background. The original supplied HTML and images in the local logo folder remain unchanged.
