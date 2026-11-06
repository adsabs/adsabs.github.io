---
layout: post_scix
title: "Mentions and Credits"
order: 7.5
---

Citations record when one paper lists another in its reference list. Software, datasets and grants are often acknowledged less formally: in a Data Availability Statement, in the text, or in the funding information a publisher supplies. SciX captures these acknowledgments as **mentions** and **credits**, so the people who build software, curate data and fund research can see the work that relied on it.

## Mentions and credits

A **mention** is a link from a SciX record to a piece of software, a dataset or a grant that it used or acknowledged. A **credit** is the same link seen from the other side.

If a paper mentions a software package, the software package is credited by that paper. SciX generates both directions together, so a record's mentions and the credits shown on the records it mentions always agree.

| Relationship | Read it as | Shown on |
|---|---|---|
| Mention | This paper used or acknowledged that software, dataset or grant | The paper's record |
| Credit | This software, dataset or grant was used or acknowledged by that paper | The software, dataset or grant's record |

## Where to find them

On an abstract page, select **Mentions** in the left menu to see the software and datasets a record mentions. On a software, dataset or grant record, select **Credits** to see the records that credit it. For a NASA or NSF proposal, for example, Credits lists the publications that acknowledge that award.

You can also sort search results by **Credit Count** to bring the most credited software, datasets and grants to the top. See [Sort Results]({{ site.baseurl }}/scixhelp/actions-scix/sort).

## What counts as a mention

For now SciX keeps the definition deliberately narrow, so that each mention can be trusted:

* **The target has its own SciX record.** SciX only links to software, datasets and grants that are indexed in SciX.
* **The link uses a persistent identifier.** A mention is made through a DOI or another well-defined identifier, not by matching a name in the text.
* **The target is software, a dataset or a grant.** Mentions of other kinds of resources are not yet tracked.

## Where mentions come from

* **Data Availability Statements.** Many journals ask authors to list the data and software behind their results. SciX extracts the links from these sections of the full text for a growing list of journals from publishers including AAS, AGU, AMS, Elsevier, IOP and Springer.
* **The Astrophysics Source Code Library (ASCL).** The [ASCL](https://ascl.net) records which papers describe or use each software package it lists, and SciX imports those links.
* **Funding metadata.** Publishers (through Crossref) and data repositories (through DataCite) often record the funder and award number behind a publication. When an award number matches a NASA or NSF proposal indexed in SciX, the publication is linked to that grant.
* **Repository and related works links.** DataCite metadata and the related works links SciX receives from other sources, including users, add a smaller number of links between publications, software and datasets.

Work is under way to find mentions anywhere in the body of a paper, not just in its Data Availability Statement.

## How mentions relate to citations and references

Mentions and credits work like [citations and references]({{ site.baseurl }}/scixhelp/search-scix/citations-and-references): a mention is the counterpart of a reference, and a credit is the counterpart of a citation. They are kept separate because they capture different things.

* **Citations and references** come from the formal reference list of a paper.
* **Mentions and credits** come from less formal acknowledgments elsewhere in a paper or its metadata. A dataset named in a Data Availability Statement but missing from the reference list appears as a mention, not a reference.

## Current limitations

Mentions and credits are a new feature, and coverage is growing rather than complete. Keep in mind:

* **A missing mention does not mean there is no connection.** The journal may not be covered yet, the link may sit outside the Data Availability Statement, or the software or dataset may not have a SciX record.
* **Software and datasets are listed together.** A record's Mentions list can mix both. To tell them apart, check the document type of each item, or filter by document type (`doctype:software` or `doctype:dataset`).
* **Mentions are not included in metrics.** Citation counts, the h-index and other indicators are based on citations only.
* **There are no search operators for mentions yet.** Operators that work like `citations()` and `references()` for mentions and credits are planned.

If you know of a link between a publication and software, data or a grant that SciX is missing, or have ideas for what you would like to do with mentions, write to us at [help@scixplorer.org](mailto:help@scixplorer.org).
