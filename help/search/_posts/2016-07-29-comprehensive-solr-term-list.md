---
layout: post
title: "Comprehensive List of Solr Fields & Operators"
order: 6
---


**This is an extensive list of methods of querying the ADS system.**
It is a technical document and you probably don't need to read it unless you are interested in performing advanced searches.

**Solr (Virtual) Fields, Operators, and Other Stuff**

An aggregated list of the fields, operators, and other parameters that are accessible from Solr. Descriptions of what they are used for, and why or where they should or should not be shown to users.


 |                     Field Name | Searchable | Retrievable | Explanation |
 |  ----------------------------- | - | - | ----------- |
 |                    \_version\_ | y | y | Integer (timestamp-like) indicating internal versioning sequence, if it has changed it means the record has been reindexed |
 |                            abs | y | y | Virtual field to search across `title`, `keyword`, `abstract` fields in one operation |
 |                       abstract | y | y | Abstract of the record |
 |                            ack | y | n | Contains acknowledgements extracted from fulltexts (if identified in article). |
 |                            aff | y | y | Affiliation strings of authors (raw data), values correspond to order of `author` field. Multiple values separated by `;`. See [canonical data](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv) for all things `aff_`|
 |                     aff_abbrev | y | y | List of curated institution abbreviations for a given paper |
 |                  aff_canonical | y | y | List of curated institution names |
 |                 aff_facet_hier | y | y | Hierarchical label consisting of `Level/Parent/Child` - i.e. `1/CSIC Madrid/Inst Phys`. List of values is *not* linked to order/number of authors. |
 |                         aff_id | y | y | List of curated affiliation IDs in a given paper, values correspond to order of `author` field. Multiple values separated by `;`|
 |                          affil | y | n | Virtual field searching across `aff_abbrev`, `aff_canonical`, `aff_id`, `institution`, `aff` |
 |              alternate_bibcode | y | y | List of alternate bibcodes for the document |
 |                alternate_title | y | y | Alternate title, usually when the original title is not in English |
 |                    arxiv_class | y | y | arXiv class the paper was submitted to |
 |                         author | y | y | List of authors on a paper (multivalued field, order is preserved; see `aff*` and `orcid*` fields for additional details) |
 |                   author_count | y | y | Number of authors on a paper (integer) |
 |                   author_facet | y | n | Contains normalized version of the author name, cannot be retrieved but useful for faceting |
 |              author_facet_hier | y | n | Hierarchical facet for author names, the levels can be used to limit result sets - i.e. `0/Surname` -> `1/Surname/N` or `1/Surname/Name` |
 |                    author_norm | y | y | List of authors with their first name initialized (see `author_facet`) |
 |                        bibcode | y | y | ADS identifier of a paper |
 |                       bibgroup | y | y | Bibliographic group that the bibcode belongs to (curated by staff outside of ADS) |
 |                 bibgroup_facet | y | n | As above, but can only be searched and faceted on |
 |                        bibstem | y | y | the abbreviated name of the journal or publication, e.g., ApJ. Full lists of bibstems can be found [here](http://adsabs.harvard.edu/abs_doc/journal_abbr.html) |
 |                  bibstem_facet | y | n | Technical field, used for faceting by publication. It contains only bibstems without volumes (eg. `Sci`) |
 |                           body | y | n | Contains extracted fulltext minus acknowledgements section |
 |                    book_author | y | y | The name will be also in `author` field; but not the other way around |
 |                        caption | y | y | Captions extracted from illustrations/tables |
 |                       citation | y | y | List of bibcodes that cite the paper |
 |                 citation_count | y | y | Number of citations the item has received |
 |            citation_count_norm | y | y | Number of citations normalized by `author_count` |
 |                cite_read_boost | y | y | Float values containing normalized (float) boost factors. These can be used with functional queries to modify ranking of results. |
 |                 classic_factor | y | y | Integer values containing the boost factor used by ADS Classic. In essence log(1 + cites + norm_reads) where number of citations has been normalized and the whole value is multiplied by 5000 and then cast to Integer. |
 |                        comment | y | y | Kitchen sink for holding various bits of information not available elsewhere (probably only useful if you are curating ADS records) |
 |                      copyright | y | y | Copyright given by the publisher |
 |                           data | y | y | List of sources that hold data associated with this paper (record) - format is `name:count`, i.e. `Chandra:3` |
 |                     data_facet | y | n | Data sources for the paper (without counts, but the counts can be retrieved when faceting on the values of this field) |
 |                       database | y | y | Database (collection) into which the paper was classified, a paper can belong to more than one|
 |                           date | y | y | Machine readable version of `pubdate`, time format: `YYYY-MM-DD'T'hh:mm:ss.SSS'Z'`|
 |                        doctype | y | y | Types of document: abstract, article, book, bookreview, catalog, circular, editorial, eprint, erratum, inbook, inproceedings, mastersthesis, misc, newsletter, obituary, phdthesis, pressrelease, proceedings, proposal, software, talk, techreport|
 |             doctype_facet_hier | y | n | Hierarchical facets consisting of nested document types |
 |                            doi | y | y | Digital object identifier |
 |                         editor | y | y | Typically for books or series, similar rules to `book_author` |
 |                            eid | y | y | Electronic id of the paper (equivalent of page number) |
 |                          email | y | n | List of e-mails for the authors that included them in the article (is only accessible to users with elevated privileges) |
 |                        entdate | y | y | Creation date of ADS record in user-friendly format (YYYY-MM-DD) |
 |                     entry_date | y | y | Creation date of ADS record in RFC 3339 (machine-readable) format |
 |                       esources | y | y | Types of electronic sources available for a record (e.g. pub_html, eprint_pdf) |
 |                       facility | y | y | List of facilities declared in paper (low count field for now) |
 |                   first_author | y | y | First author of the paper |
 |        first_author_facet_hier | y | n | See `author_facet_hier` |
 |              first_author_norm | y | n | See `author_norm` |
 |                 fulltext_mtime | y | y | Machine readable modification timestamp; corresponds to time when a fulltext was updated |
 |                          grant | y | y | Field that contains both grant ids and grant agencies. |
 |               grant_facet_hier | y | n | Hierarchical facet field which contains grant/grant_id. This field is not suitable for user queries, but rather for UI components. Term frequencies and positions are deactivated. |
 |                             id | y | y | Internal identifier of a record, does not change with reindexing but users are advised to not rely on contents of this field |
 |                     identifier | y | n | A field that can be used to search an array of alternative identifiers for the record. May contain alternative bibcodes, DOIs and/or arxiv ids. |
 |                     indexstamp | y | y | Date at which the record was indexed `YYYY-MM-DD'T'hh:mm:ss.SSS'Z'` |
 |                           inst | y | n | Virtual field to search across `aff_id`, and `institution` |
 |                    institution | y | n | List of curated affiliations (institutions) in a given paper. See [institution data](https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv)|
 |                           isbn | y | y | ISBN of the publication (this applies to books) |
 |                           issn | y | y | ISSN of the publication (applies to journals - ie. periodical publications) |
 |                          issue | y | y | Issue number of the journal that includes the article |
 |                        keyword | y | y | Array of normalized and non-normalized keywords |
 |                  keyword_facet | y | n | Like `keyword` but used for faceting |
 |                   keyword_norm | y | y | Controlled keywords, if it was identified |
 |                 keyword_schema | y | y | Schema for each controlled keyword, i.e., the schema of a `keyword` if it can be assigned |
 |                           lang | y | y | In ADS this field contains a language of the main title. Currently, this value is present in a very small portion of records |
 |                     links_data | y | y | Internal data structure with information for generating links to external sources (API users are advised to use link resolver service instead) |
 |                 metadata_mtime | y | y | Machine readable modification timestamp; corresponds to time when bibliographic metadata was updated |
 |                  metrics_mtime | y | y | Machine readable modification timestamp; corresponds to time when citations metrics were updated |
 |          ned_object_facet_hier | y | y | Hierarchical `Level/Parent/Child` entry for NED objects |
 |                          nedid | y | y | List of NED IDs within a record |
 |                        nedtype | y | y | Keywords used to describe the NED type (e.g. galaxy, star) |
 |      nedtype_object_facet_hier | y | n | Hierarchical facet consisting of NED object type and ID |
 |                   nonbib_mtime | y | y | Machine readable modification timestamp; corresponds to time when non-bibliographic metadata was updated |
 |                          orcid | y | n | Virtual field to search across all orcid fields |
 |                    orcid_mtime | y | y | Machine readable modification timestamp; corresponds to time when data were fetched from ORCiD |
 |                    orcid_other | y | y | ORCID claims from users who used the ADS claiming interface, but did not give us consent to show their profiles |
 |                      orcid_pub | y | y | ORCID IDs supplied by publishers |
 |                     orcid_user | y | y | ORCID claims from users who gave ADS consent to expose their public profiles. |
 |                           page | y | y | First page of a record |
 |                     page_count | y | y | If page_range is present, gives the difference between the first and last page numbers in the range |
 |                       property | y | y | Array of miscellaneous flags associated with the record. For possible values see [Properties](search-syntax#properties).| 
 |                            pub | y | y | Canonical name of the publication the record appeared in |
 |                        pub_raw | y | y | Name of publisher, but also includes the volume, page, and issue if they exist |
 |                        pubdate | y | y | Publication date in the form `YYYY-MM-DD` (DD value will always be "00") - corresponds to the old version of metadata timestamps (ADS Classic) |
 |                      publisher | y | y | Low frequency field, internal use |
 |                        pubnote | y | y | Comments submitted with the arXiv version of the paper |
 |                     read_count | y | y | Number of times the record has been viewed in a 90-day windows (by users from ADS and arXiv -- aggregate value) |
 |                         reader | y | n | List of (anonymized) identifiers for people who have read the article |
 |                          recid | y | y | Unique identifier of the document, Integer version of 'id' - more efficient for sorting, and range queries |
 |                      reference | y | y | List of (identified/resolved) references from the paper |
 |                         series | y | y | Information about conference series |
 |       simbad_object_facet_hier | y | y | The hierarchical facets consisting of SIMBAD `object_type/object_id` |
 |                         simbid | y | y | List of SIMBAD IDs within the paper |
 |                       simbtype | y | y | Keywords used to describe the SIMBAD type |
 |                          title | y | y | Title of the record |
 |               update_timestamp | y | y | Machine readable modification timestamp; corresponds to time when the record was reindexed |
 |                         vizier | y | y | Keywords, "subject" tags from VizieR |
 |                   vizier_facet | y | y | Contains list of VizieR keywords with the number of occurences that keyword has for the search |
 |                         volume | y | y | Volume of the journal that the article exists in |
 |                           year | y | y | Year of publication |



 |  **Functional Operators**   | **Example** | **Explanation** |
 | --------------------------- | - | - |
 |  [citations()](../search/citations-and-references)  | `citations(aff:MIT)` | Returns list of citations for papers matching the inner query; use `fl=[citations]` to retrieve the field contents |
 |  [pos()](../search/positional)                      | `pos(author:accomazzi, 1, 5)` | The pos() operator allows you to search for an item within a field by specifying the position  (range). The syntax for this operator is `pos(fieldedquery,position,[endposition])`. If no endposition is given, then it is assumed to be endposition = position, otherwise this performs a query within the range [position, endposition]. |
 |  [references()](../search/citations-and-references) | `references(author:huchra)` | Returns list of references from papers matching the inner query |
 |  [reviews()](../search/second-order)                | `reviews(title:"monte carlo")` | returns the list of documents citing the most relevant papers on the topic being researched; these are papers containing the most extensive reviews of the field. |
 |  [similar()](../search/second-order)                | `similar(title:hubble^2, abstract, 100)`<br/>`similar("hubble space telescope", input)` | Find similar documents, either based on their similarity with the documents from the inner query or similar to the text that you supplied. <br/><br/>Format: `similar(queryOrText, fields, maxQueryTerms, docToSearch, minTermFreq, minDocFreq, percentToMatch)`. <br/><br/>- `queryOrText`: string, this can be a query or input <br/>- `fields`: list of fields separated by spaces, or special token 'input' which means use the query as is, as input <br/>- `maxQueryTerms`: modifies similarity search, only this many terms will be considered during the search (those terms are NOT the first X collected, but they will be the first X terms weighted by TFIDF - term frequency/inverse document frequency) <br/>- `docToSearch`: how many documents to collect in the first phase, is ignored when fields='input' <br/>- `minTermFreq`: term is selected only if its frequency is this or higher - minDocFreq: selected term must be present in at least that many documents <br/>- `percentToMatch`: ratio of terms that have to be present in the selected documents, default is 0.0f. For example, if 100 terms was used to discover similar docs, and if the ratio was 0.3f - then 30 terms must be present in the docs that are returned. |
 |  [topn()](../search/second-order)                   | `topn(200, citations(title:hubble), citation_count desc)` | Limit results to the best top N (by their ranking or sort order); format: `topn(int, query, 'sort order')`. If the sort order is not specified, the default `score desc` will be used. |
 |  [trending()](../search/second-order)               | `trending("machine learning")` | Trending – returns the list of documents most read by users who read recent papers on the topic being researched; these are papers currently being read by people interested in this field. |
 |  [useful() ](../search/second-order)                | `useful("gradient descent")` | Useful – returns the list of documents frequently cited by the most relevant papers on the topic being researched; these are studies which discuss methods and techniques useful to conduct research in this field. |
 |  docs()                                          | `docs(library/hHGU1Ef-TpacAhicI3J8kQ)` | Retrieve set of documents specified by their IDs. You can think of this as a set operator; it will fill the set with documents that correspond to identifiers that are passed in. And this set can then be combined with other queries (i.e. `docs(A) NOT author:huchra`) |
