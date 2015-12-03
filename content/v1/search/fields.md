---
title: Query Fields | ADS API
---

# Fields and Indexes


The following represents exhaustive list of search fields. Some fields are meant only for searches, some just store
values, but majority does fullfil both functions.

**NOTE**: field type `I` means field can be searched, `S` values can be retrieved

field           |  field type      | note 
----------------|------------------|----------------------------------
`author`        |IS| array of strings |  IS  | Ordered list of author names. Normalized, UTF-8 compatible.
`bibcode`       |IS| the canonical ADS bibcode identifier for this record
`bibstem`       |IS|  the abbreviated name of the journal or publication, e.g., *ApJ*.
`id`            |IS| a unique integer for this record
`identifier`    |IS| an array of alternative identifiers for the record. May contain alternative bibcodes, DOIs and/or arxiv ids.
`title`         |IS| the title of the record
`author`        |IS| an array of the author names associated with the record
`pub`           |IS| the canonical name of the publication the record appeared in
`keyword`       |IS| an array of normalized and un-normalized keyword values associated with the record
`abstract`      |IS| the abstract of the record
`aff`	        |IS| an array of the authors' affiliations
`property`      |IS| an array of miscellaneous flags associated with the record. Possible values include: ARTICLE, REFEREED, NOT_REFEREED, INPROCEEDINGS, OPENACCESS, NONARTICLE, EPRINT, BOOK, PROCEEDINGS, CATALOG, SOFTWARE
`volume`        |IS|  volume the record appeared in
`issue`         |IS|  issue the record appeared in
`page`          |IS|  starting page
`citation_count`|IS|  number of citations the item has received
`read_count`    |IS|  number of times the record has been viewed within in a 90-day windows (ads and arxiv)
`pubdate`       |IS|  publication date in the form YYYY-MM-DD (DD value will always be "00")
`database`      |IS|  which database the record is associated with. The ADS content is divided into a few separate databases: "astronomy", "physics" & "general". By default, queries will return results from all three. To limit a search to "astronomy" articles, add `fq=database:astronomy` to the request parameters.


