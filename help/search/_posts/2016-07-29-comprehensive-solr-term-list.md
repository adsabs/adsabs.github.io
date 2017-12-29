---
layout: post
title: "Comprehensive List of Solr Fields & Operators"
order: 6
---


**This is an extensive list of methods of querying the ADS system.**
It is a technical document and you probably don't need to read it unless you are interested in performing advanced searches.

**Solr (Virtual) Fields, Operators, and Other Stuff**

An aggregated list of the fields, operators, and other parameters that are accessible from Solr. Descriptions of what they are used for, and why or where they should or should not be shown to users.


| Field Name | Deprecated | Useful for user | Show/Give access? [y/n] | Explanation |
| ---------- | ---------- | --------------- | ----------------------- | ----------- |
| abstract | n | y | y | the abstract of the record |
| ack | n | y | y | Contains acknowledgements extracted from fulltexts (if identified in article). |
| aff | n | y | y | List of author affiliations in a given paper |
| alternate_bibcode | n | y | y | List of alternate bibcodes for that document |
| alternate_title | n | y | y | Alternate title, usually when the original title is not in English  |
| arxiv_class | n | y | y | Which arXiv class was the paper submitted to |
| author | n | y | y | List of authors on a paper |
| author_count | n | y | y |  Number of authors on a paper |
| author_facet | n | y&n | y&n | Contains list of names with the number of occurences that author has for the search (can only be searched) |
| author_facet_hier | n | n | n | Hierarchical facet field which contains author/author_id. |
| author_norm | n | n | n | List of authors with their first names shortened? |
| bibcode | n | y | y | ADS identifier of a paper |
| bibgroup | n | y | y | Bibliographic group that the bibcode belongs to (curated by staff outside of ADS) |
| bibgroup_facet | n | y&n | y&n | Contains list of groups with the number of occurrences that group has for the search |
| bibstem | n | y | y | the abbreviated name of the journal or publication, e.g., ApJ. |
| bibstem_facet | n | n | n | Technical field, used for faceting by publication. It contains only bibstems without volumes (eg. Sci) |
| body | n | y | n | Contains extracted fulltext minus acknowledgements section |
| citation | n | y | n | List of bibcodes that cite the paper |
| citation_count | n | y | y | number of citations the item has received |
| cite_read_boost | n | n | n | Float values containing normalized (float) boost factors. These can be used with functional queries to modify ranking of results. |
| classic_factor | n | n | n | Integer values containing the boost factor used by ADS Classic. In essence log(1 + cites + norm_reads) where number of citations has been normalized and the whole value is multiplied by 5000 and then cast to Integer. |
| comment | n | y | tbd | This is currently indexed, but not stored. To see the values, Solr needs to also store it. |
| copyright | n | y | y | Copyright given by the publisher |
| data | n | y | y | List of sources that have data related to this bibcode |
| data_facet | n | y&n | y&n | Contains list of data with the number of occurrences that data has for the search |
| database | n | y | y | Database that the paper resides in (astronomy or physics)|
| date | n | n | n | Same as pubdate, but of time format and used for indexing; too excessive for a user to care about/use |
| doctype | n | n | n | Type of document: article, thesis, etc, these stem from classic |
| doctype_facet_hier | n | y&n | y&n | Hierarchical facets consisting of nested document types |
| doi | n | y | y | Digital object identifier |
| eid | n | y | y | electronic id of the paper (equivalent of page number) |
| email | n | y | n | List of e-mails for the authors that included them in the article; protect due to privacy concerns - difficult to stop unless we stop people seeing it now |
| entry_date | n | y | y | Creation date of ADS record |
| esources | n | y | y | Types of electronic sources available for a record (e.g. pub_html, eprint_pdf) |
| facility | n | y | tbd | List of facilities declared in paper (controlled list for AAS journals so far). Needs to be added in ADSImportpipeline and Solr schemas |
| first_author | n | y | y | First author of the paper |
| first_author_facet_hier | n | y&n | y&n | Contains list of first names with the number of occurrences that author has for the search, contains author/author_id |
| first_author_norm | n | n | n | First author of the paper with their first name shortened? |
| grant | n | y | y | Field that contains both grant ids and grant agencies. |
| grant_agencies | y | n | n | Index with just the grant agencies names (e.g. NASA). |
| grant_facet_hier | n | n | n | Hierarchical facet field which contains grant/grant_id. This field is not suitable for user queries, but rather for UI components. Term frequencies and positions are deactivated. |
| grant_id | y | n | n | Index with just the grant ids (e.g. 0618398) |
| id | n | n | y | a unique integer for this record. Generally not useful, but used by Andy Casey's python client |
| identifier | n | y | y | an array of alternative identifiers for the record. May contain alternative bibcodes, DOIs and/or arxiv ids. |
| ids_data | ? | ? | ? | https://github.com/adsabs/issues/issues/73 |
| indexstamp | n | y | y | Date at which the document was indexed by Solr YYYY-MM-DD'T'hh:mm:ss.SSS'Z' |
| isbn | n | y | tbd | ISBN of the publication (this applies to books) |
| issn | n | y | tbd | ISSN of the publication (applies to journals - ie. periodical publications) |
| issue | n | y | y | Issue number of the journal that includes the article |
| keyword | n | y | y | an array of normalized and non-normalized keyword values associated with the record |
| keyword_facet | n | y&n | y&n | Contains list of keywords with the number of occurrences that keyword has for the search |
| keyword_norm | n | n | n | Controlled keywords, each entry will have a corresponding keyword_schema entry |
| keyword_schema | n | y | y | Schema for each controlled keyword, i.e., what was the origin of the keyword? |
| lang | n | y | y | In ADS this field contains a language of the main title. Currently, this value is present in a very small portion of records (try searching for lang:*) |
| links_data | n | n | n | We use it to contain info on what readable linked documents are available? |
| nedid | n | y | y | List of NED IDs within a record |
| nedtype | n | y | y | Keywords used to describe the NED type (e.g. galaxy, star) |
| nedtype_object_facet_hier | n | y&n | y&n | Hierarchical facet consisting of NED object type and ID |
| orcid_other | n | y | y | ORCID claims from users who used Bumblebee claiming interface, but did not give us consent to show their profiles |
| orcid_pub | n | y | y | ORCID IDs supplied by publishers |
| orcid_user | n | y | y | ORCID claims from users who gave ADS consent to expose their public profiles. |
| page | n | y | y | First page of a record |
| page_count | n | y | y | If page_range is present, gives the difference between the first and last page numbers in the range |
| page_range | n | n | n | Range of page numbers covered by the record |
| property | n | y | y | an array of miscellaneous flags associated with the record. Possible values include: ARTICLE, REFEREED, NOT_REFEREED, INPROCEEDINGS, OPENACCESS, NONARTICLE, EPRINT, BOOK, PROCEEDINGS, CATALOG, SOFTWARE |
| pub | n | y | y | the canonical name of the publication the record appeared in |
| pub_raw | n | n | n | Name of publisher, but also includes the volume, page, and issue if exists |
| pubdate | n | y | y | publication date in the form YYYY-MM-DD (DD value will always be "00") - May be interesting for people who want publication month |
| pubnote | n | n | n | Comments submitted with the arXiv version of the paper |
| read_count | n | y | y | number of times the record has been viewed within in a 90-day windows (ads and arxiv); len(readers) |
| reader | n | y | n | List of identifiers for people who have read the article |
| recid | n | n | n | Unique identifier of the document, Integer version of 'id' - this is more efficient for sorting, and range queries |
| reference | n | y | n | List of references inside a paper |
| simbad_object_facet_hier | n | y&n | y&n | The hierarchical facets consisting of object_type/object_id  |
| simbid | n | y | y | List of SIMBAD IDs within the paper. This has privacy restrictions |
| simbtype | n | y | y | Keywords used to describe the SIMBAD type |
| thesis | ? | ? | ? | https://github.com/adsabs/issues/issues/72 |
| title | n | y | y | the title of the record |
| vizier | n | y | y | Keywords, "subject" tags from VizieR |
| vizier_facet | n | y&n | y&n | Contains list of VizieR keywords with the number of occurences that keyword has for the search |
| volume | n | y | y | Volume of the journal that the article exists in |
| year | n | y | y | Year of publication |
| **Virtual Fields/Operators** |  |  |  |  |
| abs | n | y | y | Combination of the following: abstract, title, keyword |
| all | n | n | n | this combines the following: author_norm, alternate_title, bibcode, doi, identifier |
| arxiv | n | y | y | query parser token |
| citations() | n | y | y | returns list of citations from given papers |
| citis() | y | n | n | Different implementation of citation(), less memory but slower |
| classic_relevance() | n | n | n | Toy-implementation of the ADS Classic relevance score algorithm. You can wrap any query and obtain the hits sorted in the ADS Classic ways (sort of) |
| full | n | y | y | this combines the following: title^2, abstract^2, body, keyword, ack |
| instructive() | y | n | n | Synonym of reviews() |
| joincitations() | y | n | n | Equivalent of citations() but implemented using lucene block-join |
| joinreferences() | y | n | n | Equivalent of references() but implemented using lucene block-join |
| orcid | n | y | y | this combined the following: orcid_pub, orcid_user, orcid_other |
| pos() | n | y | y | The pos() operator allows you to search for an item within a field by specifying the position in the field. The syntax for this operator is pos(fieldedquery,position,[endposition]). If no endposition is given, then it is assumed to be endposition = position, otherwise this performs a query within the range [position, endposition]. |
| references() | n | y | y | returns list of references from given papers |
| reviews() | n | y | y | returns the list of documents citing the most relevant papers on the topic being researched; these are papers containing the most extensive reviews of the field. |
| reviews2() | y | n | n | Original implementation of reviews |
| topn() | n | y | y | Return the top N number of documents |
| trending() | n | y | y | Trending – returns the list of documents most read by users who read recent papers on the topic being researched; these are papers currently being read by people interested in this field. |
| useful() | n | y | y | Useful – returns the list of documents frequently cited by the most relevant papers on the topic being researched; these are studies which discuss methods and techniques useful to conduct research in this field. |
| useful2() | y | n | n | What experts are citing; original implementation of useful()|
| **Field Name** | **Deprecated** | **Useful for user** | **Show/Give access? [y/n]**
