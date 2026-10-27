# Maintaining the Neuropia website

The website uses al-folio with group content stored separately from its example content. The default navigation is Home, People, Publications, and Contact. The homepage is labeled Home in the navigation and displays Neuropia as its heading.

## Members

Edit `_data/members.yml`. Entries appear in file order. Names and initials are sufficient; no role or individual affiliation is inferred. Optional fields are `role`, `bio`, `image`, `email`, `orcid`, and `website`. Store photos under `assets/img/` and set `image` to the filename. Supply the bare ORCID identifier and a complete HTTPS URL for `website`. Initials appear when no photo is supplied.

## Affiliations

Edit `_data/affiliations.yml`. The homepage and Contact page read the same list. These describe group affiliations, not affiliations assigned to each individual member.

## Publications

Add verified BibTeX records to `_bibliography/neuropia.bib`. The Publications page displays an explanatory message until the bibliography has entries, then renders the bibliography in descending year order. The template's `papers.bib` is retained as an example and is not used for group publications.

## Research and news

Add research themes, project descriptions, and news once approved group content is available. Template examples remain in the repository but are excluded from the website through `_config.yml`; remove the relevant exclusions when replacing those examples with real content. External example feeds are disabled.

## Build and deployment

The current project site uses `url: https://traixthetroll.github.io` and `baseurl: /neuropia.github.io`. Use `relative_url` for internal links so the project prefix is preserved. Run `bundle exec jekyll build` with the configured base URL. Merging changes into `main` triggers the existing GitHub Pages deployment.

Site-specific styles live in `assets/css/neuropia.css` and are loaded only by the homepage and People page. No gem-owned layout or include is overridden.
