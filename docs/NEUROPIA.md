# Maintaining the Neuropia website

The website uses al-folio with group content stored separately from its example content. The default navigation is Home, Research, People, Publications, and Contact. The homepage is labeled Home in the navigation and displays Neuropia as its heading.

## Members

Edit `_data/members.yml`. Entries appear in file order. Current roles were supplied by the group; individual affiliations are not assigned. Optional fields are `role`, `bio`, `image`, `email`, `orcid`, `linkedin`, and `website`. Store photos under `assets/img/` and set `image` to the filename. Supply the bare ORCID identifier and complete HTTPS URLs for `linkedin` and `website`. Initials appear when no photo is supplied. Current member images are in `assets/img/people/`. Supplied TIFF and PNG files were converted to JPEG at their original pixel dimensions; supplied WebP images are used unchanged. The source images remain unchanged in the supplied folder.

Each member has a stable `slug` and an individual Markdown page at `_pages/member-<slug>.md`, published under `/people/<slug>/`. The People cards link to these pages. Edit the short About section on each page to replace its placeholder with a biography. Images and roles are read from `_data/members.yml`; profile pages preserve each image's full aspect ratio. Profile photos are not clickable and have no full-size-image caption. Directory thumbnails use a square crop for a consistent grid.

Member profiles use About, optional Research interests, and optional Links sections. Current work and per-person Selected publications sections are omitted. Casper’s page provides the first completed example. Individual profiles display LinkedIn, ORCID, and institutional profile links first, followed by a separate Email line. The full email address remains visible and selectable and links to a `mailto:` target. These details come from `_data/members.yml`; missing details are hidden. The People directory links to each member’s profile without displaying contact or social links.

The main page headings and navigation brand use a bold font weight in `assets/css/neuropia.css`.

## Affiliations

Edit `_data/affiliations.yml`. The homepage and Contact page read the same list. These describe group affiliations, not affiliations assigned to each individual member. Neuro-SysMed’s `url` is used only for its link in the homepage introduction. Names in the Affiliations section remain plain text.

## Publications

New public ORCID journal articles are checked daily and proposed in a review PR. See [Publication synchronization](PUBLICATION_SYNC.md) for coverage, review, exclusions, and manual runs. The automation never merges publication proposals automatically.

Edit `_bibliography/neuropia.bib`. The initial selection contains eight PubMed-verified publications from 2022–2026, with DOI, PubMed, and PMC full-text links. The Publications page renders entries in descending year order and displays an explanatory message if the bibliography is empty. The template's `papers.bib` is retained as an example and is not used for group publications. The optional inline publication filter is disabled because the pinned template version raises a browser error during input; site search remains enabled. See `sources/README.md` for queries, screening decisions, metadata, and editorial limits. The sources directory is excluded from the website build.

## Research and news

Research themes are introduced on the homepage and in `_pages/research.md`. Keep research interests distinct from demonstrated findings, and preserve the links supporting study descriptions. The current page distinguishes clinical, cell-culture, animal-model, and review evidence. Add project descriptions and news when group content is available. Template examples remain in the repository but are excluded from the website through `_config.yml`; remove the relevant exclusions when replacing those examples with real content. External example feeds are disabled.

## Build and deployment

The current project site uses `url: https://traixthetroll.github.io` and `baseurl: /neuropia`. Use `relative_url` for internal links so the project prefix is preserved. Run `bundle exec jekyll build` with the configured base URL. Merging changes into `main` triggers the existing GitHub Pages deployment.

Site-specific styles live in `assets/css/neuropia.css` and are loaded by all public pages. Include the same stylesheet when adding a page. No gem-owned layout or include is overridden.

## Logo and palette

`assets/img/neuropia-logo.png` is an unchanged copy of the group-supplied transparent PNG (`NEUROPIA vektor gjennomsiktig.png`, 3000 × 3000 pixels). It appears in the homepage introduction, beside the navigation brand on inner pages, and as the favicon. The original transparency and proportions are preserved.

The site's accent colors come from the logo: navy `#0f2033`, teal `#2c7a77`, and warm gold `#facc8a`. Light mode uses teal links and accents; dark mode uses a navy background and gold accents. Color variables and responsive logo sizing are in `assets/css/neuropia.css`.

The decorative neuron background at `assets/img/backgrounds/dm-wallpaper.png` is an unchanged copy of the supplied transparent `BACKGROUNDS/DM_wallpaper.png` (1448 × 1086 pixels). A fixed CSS layer places it behind page content in both color modes, centered and repeated in 900-pixel-wide tiles so individual neurons appear smaller than the previous viewport-covering image. Its opacity is controlled by `--neuropia-background-opacity: 0.03` in `assets/css/neuropia.css`. The layer ignores pointer events so navigation and page controls remain usable.
