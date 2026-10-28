# ORCID identities and import provenance

Identity checks were performed on 28 October 2026. ORCID records were read directly from the public v3.0 API. Names were checked against the supplied group membership, and at least one DOI in each record was matched to the existing verified group bibliography. No ORCID was assigned using a name-only search result.

| Member                    | Verified ORCID                                                               | Matching DOI                                                                 |
| ------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Christopher Elnan Kvistad | [0000-0002-8393-2772](https://pub.orcid.org/v3.0/0000-0002-8393-2772/record) | [10.3390/ijms251910292](https://doi.org/10.3390/ijms251910292)               |
| Torbjørn Kråkenes         | [0000-0002-4031-5360](https://pub.orcid.org/v3.0/0000-0002-4031-5360/record) | [10.1371/journal.pone.0347119](https://doi.org/10.1371/journal.pone.0347119) |
| Marie Ytterdal            | [0009-0004-6032-7600](https://pub.orcid.org/v3.0/0009-0004-6032-7600/record) | [10.1371/journal.pone.0347119](https://doi.org/10.1371/journal.pone.0347119) |
| Casper Eugen Sandvik      | [0009-0002-5931-7670](https://pub.orcid.org/v3.0/0009-0002-5931-7670/record) | [10.1371/journal.pone.0347119](https://doi.org/10.1371/journal.pone.0347119) |
| Lars Bø                   | [0000-0001-8675-4433](https://pub.orcid.org/v3.0/0000-0001-8675-4433/record) | [10.1212/WNL.0000000000214915](https://doi.org/10.1212/WNL.0000000000214915) |

Casper's identifier was supplied by the group and independently confirmed. The other four identifiers were confirmed against public ORCID names and known publication DOIs. Andrea Gremes, Christian Grønås, and Anna-Maria Rasmussen Eitrheim have no verified identifiers configured yet; this does not imply they have no ORCID or publications.

`imports.json` records DOI, title, year, matched members, and the Crossref metadata endpoint for each addition made through the synchronization workflow. Existing curated publications retain their original PubMed provenance in the parent directory. No abstracts are copied. This entire directory is excluded from the public website.
