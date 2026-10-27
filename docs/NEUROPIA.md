# Maintaining the Neuropia website

The website uses al-folio with group content stored separately from its example content. The default navigation is Home, Research, People, Publications, and Contact. The homepage is labeled Home in the navigation and displays Neuropia as its heading.

## Members

Edit `_data/members.yml`. Entries appear in file order. Current roles were supplied by the group; individual affiliations are not assigned. Optional fields are `role`, `bio`, `image`, `email`, `orcid`, and `website`. Store photos under `assets/img/` and set `image` to the filename. Supply the bare ORCID identifier and a complete HTTPS URL for `website`. Initials appear when no photo is supplied.

## Affiliations

Edit `_data/affiliations.yml`. The homepage and Contact page read the same list. These describe group affiliations, not affiliations assigned to each individual member.

## Publications

Edit `_bibliography/neuropia.bib`. The initial selection contains eight PubMed-verified publications from 2022–2026, with DOI, PubMed, and PMC full-text links. The Publications page renders entries in descending year order and displays an explanatory message if the bibliography is empty. The template's `papers.bib` is retained as an example and is not used for group publications. The optional inline publication filter is disabled because the pinned template version raises a browser error during input; site search remains enabled. See `sources/README.md` for queries, screening decisions, metadata, and editorial limits. The sources directory is excluded from the website build.

## Research and news

Research themes are introduced on the homepage and in `_pages/research.md`. Keep research interests distinct from demonstrated findings, and preserve the links supporting study descriptions. The current page distinguishes clinical, cell-culture, animal-model, and review evidence. Add project descriptions and news when group content is available. Template examples remain in the repository but are excluded from the website through `_config.yml`; remove the relevant exclusions when replacing those examples with real content. External example feeds are disabled.

## Build and deployment

The current project site uses `url: https://traixthetroll.github.io` and `baseurl: /neuropia.github.io`. Use `relative_url` for internal links so the project prefix is preserved. Run `bundle exec jekyll build` with the configured base URL. Merging changes into `main` triggers the existing GitHub Pages deployment.

Site-specific styles live in `assets/css/neuropia.css` and are loaded only by the homepage and People page. No gem-owned layout or include is overridden.
