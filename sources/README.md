# PubMed verification for the Neuropia website

Search and verification date: **27 October 2026**.

This is a focused selection for the group website, not a systematic literature review or a complete bibliography of every member. The group name, current membership, roles, affiliations, and stated interest in Parkinson's disease were supplied by the group. Research descriptions were informed by the abstracts and metadata of the publications below.

## Search and screening

The official NCBI E-utilities `esearch` and `efetch` endpoints were used directly. The research lookup skill's optional third-party API credentials were unavailable; no third-party research backend was needed for PubMed verification.

Main query:

```text
(Kvistad CE[Author] OR Krakenes T[Author] OR Ytterdal M[Author] OR Sandvik CE[Author] OR Gremes A[Author] OR Gronas C[Author]) AND ("2021/01/01"[Date - Publication] : "2026/10/27"[Date - Publication])
```

The query returned **27 records**. After checking full author names, five were excluded because they involved **Trond-André Kråkenes**, a different person from **Torbjørn Kråkenes**. Eight records were selected for their relevance to MSCs, EVs, MS, and neural regeneration. The other 14 were outside this focused selection. Their exclusion does not mean those publications are unrelated to the members' wider work.

A supplementary all-date search checked `Gremes Andrea`, `Gremes A`, `Gronas Christian`, `Gronas C`, `Grønås Christian`, and `Grønås C` in author fields. It returned no records. This does not establish that Andrea Gremes or Christian Grønås has no publications: author variants, indexing coverage, and unpublished or unindexed work remain possible. No publications were assigned to them without a verified author match.

Search responses, per-record screening decisions, and metadata for the eight selected publications are saved alongside this file. The metadata preserve full author lists, journal and article dates, identifiers, and source URLs. Article abstracts are not reproduced in this repository. Bibliography years use the journal publication year.

## Selected publications

| PMID                                                  | Year | Scope / study type                                                    | DOI                                                                          |
| ----------------------------------------------------- | ---- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [42081777](https://pubmed.ncbi.nlm.nih.gov/42081777/) | 2026 | SMART-MS; randomized clinical trial                                   | [10.1212/WNL.0000000000214915](https://doi.org/10.1212/WNL.0000000000214915) |
| [42008439](https://pubmed.ncbi.nlm.nih.gov/42008439/) | 2026 | MSC neural/glial transdifferentiation; laboratory cell study          | [10.1371/journal.pone.0347119](https://doi.org/10.1371/journal.pone.0347119) |
| [40589765](https://pubmed.ncbi.nlm.nih.gov/40589765/) | 2025 | Blood biomarkers and brain-derived EVs in MS; review                  | [10.3389/fimmu.2025.1569503](https://doi.org/10.3389/fimmu.2025.1569503)     |
| [39408622](https://pubmed.ncbi.nlm.nih.gov/39408622/) | 2024 | MSC-derived vesicles in MS; narrative review                          | [10.3390/ijms251910292](https://doi.org/10.3390/ijms251910292)               |
| [38803647](https://pubmed.ncbi.nlm.nih.gov/38803647/) | 2024 | Human CNS regeneration; review                                        | [10.3389/fneur.2024.1398089](https://doi.org/10.3389/fneur.2024.1398089)     |
| [38338644](https://pubmed.ncbi.nlm.nih.gov/38338644/) | 2024 | MSC neuroprotective mechanisms in MS; review                          | [10.3390/ijms25031365](https://doi.org/10.3390/ijms25031365)                 |
| [37943848](https://pubmed.ncbi.nlm.nih.gov/37943848/) | 2023 | MSCs in a mouse demyelination model; preclinical study                | [10.1371/journal.pone.0293908](https://doi.org/10.1371/journal.pone.0293908) |
| [35711260](https://pubmed.ncbi.nlm.nih.gov/35711260/) | 2022 | MSC clinical safety and efficacy; systematic review and meta-analysis | [10.3389/fneur.2022.891514](https://doi.org/10.3389/fneur.2022.891514)       |

## Editorial safeguards

- Roles come from the group, not inferred author order or affiliations.
- Publications are labeled as a selection by current members, including collaborative work; historical papers are not automatically presented as work performed under the Neuropia name.
- General site copy uses extracellular vesicles. Bibliographic titles preserve the source terminology, including “exosomes.”
- In vitro differentiation and mouse-model findings are not described as established patient benefit.
- The SMART-MS description states that the primary outcome did not detect a neuroregenerative effect and that safety concerns were reported.
- Parkinson's disease is described as a group-supplied research interest. No verified Parkinson's publication was added from the screened records.
- The public website excludes `sources/`; the records remain available in the repository for editorial review and future updates.
