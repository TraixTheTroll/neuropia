# Neuropia documentation

Start with the guides for this website:

- [Repository README](../README.md): current content map, runtime versions, local preview, validation, and deployment.
- [Maintaining Neuropia](NEUROPIA.md): member profiles, thumbnail regeneration/crops, the group photograph, publications, branding, animations, and site checks.
- [Publication synchronization](PUBLICATION_SYNC.md): ORCID coverage, proposal review, exclusions, and manual runs.
- [Publication provenance](../sources/README.md): source searches, identity checks, and editorial decisions.
- [Agent guidelines](../AGENTS.md): scope and requirements for automated edits.

## Inherited al-folio reference

The other guides describe the original `al-folio` v1.x starter and its plugin architecture. They may mention example content, Docker files, workflows, plugin catalogs, or commands that Neuropia no longer includes. Use the guides above for this site's setup and checks. Neuropia uses `https://neuropia.no`, an empty `baseurl`, and the custom `neuropia` layouts.

These inherited references remain useful when investigating the underlying framework or deliberately adding a feature:

- [Architecture](ARCHITECTURE.md): core runtime, configuration contracts, and local overrides.
- [Ownership boundaries](BOUNDARIES.md): gem-owned versus site-owned behavior.
- [Customization](CUSTOMIZE.md): upstream configuration and feature background.
- [Troubleshooting](TROUBLESHOOTING.md): general Jekyll/plugin debugging.
- [FAQ](FAQ.md): upstream questions and known constraints.
- [SEO](SEO.md): background on search and sharing metadata.
- [Analytics](ANALYTICS.md): optional analytics features.

Runtime plugins come from the [al-org-dev organization](https://github.com/al-org-dev). Neuropia's namespaced templates, CSS, and JavaScript are intentional site-owned customizations. Adding or removing a plugin requires matching changes to `Gemfile` and `_config.yml`.
