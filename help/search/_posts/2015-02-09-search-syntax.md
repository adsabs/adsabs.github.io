---
layout: post
title: "Search Syntax"
order: 1
---


### Search Basics

ADS's one box search form supports both fielded and unfielded queries.  Queries without fields will search the metadata and the full text of the publications, which may not produce the expected results.  For instance, if you are searching for papers by the author Marc Mars, you want to search for **author:"Mars, M"** instead of **Marc Mars** to make sure that you don't return papers that simply have the words "Marc" and "Mars" somewhere in the body of the article.

### Fielded Searches

Above the search box we supply shortcuts to frequently used search fields.  Simply click on the field that you wish to search and enter your search term in the provided location (generally between the supplied quotation marks).  Alternatively, if you start entering the name of a field an autocomplete feature will suggest a list of possible search fields.  You may string several search terms or use the filters provided with your results to help narrow the search selection.  For instance if you want to find articles published between 1980 and 1990 by John Huchra, you can use:

    author:"Huchra, John" year:1980-1990

To get you started, here is a list of search examples for commonly used fields:

Example Query                        | Explanation
-------------------------------------|------------------------------------------------------------
author:"huchra, john"                | search for papers written by an author
author:"^huchra, john"               | limit search to first-author papers
abs:"dark energy"                    | search for the phrase "dark energy" in abstract and title
year:2000                            | search for publications written in 2000
year:2000-2005                       | search for publications written between 2000 and 2005 (inclusive)
body:"gravitational waves"           | search for papers containing the phrase "gravitational waves" in the body of an article
full:"gravitational waves"           | search for papers containing the phrase "gravitational waves" in a number of fields (title, abstract, body, acknowledgements and keywords)
bibstem:ApJ                          | select papers published in a particular publication
object:((SMC OR LMC) AND M31)        | using the SIMBAD object search, find papers tagged with either SMC or LMC and M31

The rest of this page goes over the search syntax and fields indexed in our database.

### Combining Search Terms to Make a Compound Query

You can string together any number of search terms to develop a query.  By default search terms will be combined using AND as the default boolean operator, but this can be changed by explicitly specifying OR beween them.  Similarly one can exclude a term by prepending a "-" sign to it (or using the boolean "NOT").  Multiple search words or phrases may be grouped in a fielded query by enclosing them in parenthesis.  Some examples:

Example Query                        | Results
-------------------------------------|--------------------------------------------------------------
abs:(QSO "dark energy")              | papers containing both "QSO" and "dark energy" in their abstract
abs:(QSO OR "dark energy")           | papers containing either "QSO" or "dark energy in their abstract
author:"huchra, j" abs:cfa           | papers by J. Huchra which have "cfa" in their abstract
author:"huchra, j" OR abs:"great wall" | papers by J. Huchra or which mention "great wall" in their abstract
author:"huchra, j" -title:2mass      | papers by "J. Huchra" but excludes ones with "2mass" in their title
author:"huchra, j" NOT title:2mass   | same as above

### Synonyms and Acronyms

By default most search terms in ADS are expanded by adding a list of words which are synonyms of the search term.  So for example, a search of "star" in the title field will be expanded to include words such as "stars," "stellar," "starry," "starlike," and so on.  (Notice that this often includes words in foreign languages such as "etoile," "stern," and "stella"). While this feature improves recall, it sometimes compromises the precision of the results.  Our search engine allows one to turn off the synonym expansion feature by simply prepending an "=" sign in front of the search term.

Our search engine also identifies acronyms during indexing and searching (defined as words consisting entirely of uppercase characters).  A search for an uppercase word will only match documents which contain that acronym, whereas a search for a lowercase word will match documents which contain any variation of the word, irregardless of its case.  Acronyms can themselves have synonyms (for example "ADS" and "Astrophysics Data System" are synonyms), so one should be aware that there is an interaction between case-sensitiveness and synonym expansion.  The examples below illustrate these effects:

Example Query                         | Results
--------------------------------------|-------------------------------------------------------------------
title:star                            | title contains "star", any of its synonyms, or the acronym "STAR"
title:etoile                          | title contains "star" or any of its synonyms (etoile being a synonym of star); <br>the results differ from above since "STAR" is not searched for
=title:star                           | title contains "star" or the acronym "STAR"
=title:etoile                         | title contains "etoile"
title:STAR                            | title contains the acronym "STAR"
title:(=star -STAR)                | title contains "star" but not the acronym "STAR"
fuse                                  | the word "fuse" or acronym "FUSE" appear anywhere in the paper
FUSE                                  | the acronym "FUSE" appears anywhere in paper

### Author Searches

Synoym expansion also applies to author names, which provide a way to account for changes in a person's name and/or different spellings due to transliterations.  In addition to this, the default author search in ADS is "greedy" in the sense that it will retun all documents in which an author signature may match the input search string.  This allows, for instance, to have an author search for "Huchra, John" to return papers where the author name appears as "Huchra, John" or "Huchra, J."  By prepending the "=" character to the author search one can disable this feature (as well as any additional synonym expansion) and require an exact match on the author name.  Some examples:

<table>
  <tbody>
    <tr>
      <th>Example Query</th>
      <th>Results</th>
    </tr>
    <tr>
        <td>author:"murray, s"</td>
        <td>Least precise variations: finds records authored by any of the following:<ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S. </li><li>Murray, S.</li><li>Murray, Stephen D.</li><li>Murray, S. D.</li><li>Murray, Sarah S.</li><li>Murray, Scott</li><li>...</li></ul> (any possible combination with last name "murray" and first name starting with S) </td>
    </tr>
    <tr>
        <td>author:"murray, stephen"</td>
        <td>More precise variations: finds record authored by any of the following: <ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S.</li><li>Murray, S.</li><li>Murray, Stephen D.</li><li>Murray, S. D.</li><li>...</li></ul>(any possible variation of "Murray, Stephen" with or without middle name)</td>
    </tr>
    <tr>
        <td>author:"murray, stephen s"</td>
        <td>Most precise variations: finds record authored by any of the following: <ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S.</li><li>Murray, S.</li></ul>(any possible variation of "Murray, Stephen S" but no others)</td>
    </tr>
    <tr>
        <td>=author:"murray, s"</td>
        <td>Matches only records authored by "Murray, S."</td>
    </tr>
    <tr>
        <td>=author:"murray, stephen"</td>
        <td>Matches only records authored by "Murray, Stephen"</td>
    </tr>
    <tr>
        <td>=author:"murray, stephen s"</td>
        <td>Matches only records authored by "Murray, Stephen S."</td>
    </tr>
  </tbody>
</table>

As a general rule we recommend to use the full name of the person for author searches since as can be seen above the matching rules in ADS are designed to find the maximal set of records consistent with the author specification given by the user.  Rather than disabling the name-variation algorithm described above, we recommend performing refinement of search results via the user interface filters for author names as described in the ["Filter your search" section]({{ site.baseurl }}/help/search/filter).


### Available Fields

This is a list of fields currently recognized by the ADS search engine and the preferred search format:

Field Name   | Syntax                      | Example                 | Notes
------------ | --------------------------- | ----------------------- | --------------
Abstract/Title     | abs:"phrase"                | abs:"dark energy"       | search for word or phrase in abstract & title
Acknowledgements | ack:"phrase"            | ack:"ADS"                     | search for a word or phrase in the ackknowledgements
Affiliation  | aff:"phrase"                | aff:"harvard"           | search for word or phrase in affiliation field
Abstract     | abstract:"phrase"           | abstract:"dark energy"        | search for a word or phrase in an abstract only
Alternate Bibcode | alternate_bibcode:adsbib | alternate_bibcode:2003AJ....125..525J | finds articles that used to (or still have) this bibcode
Alternate Title | alternate_title:"phrase" | alternate_title:"Gammablitz" | search for a word or phrase in an articles title if they have more than one, in multiple languages
arXiv ID     | arXiv:arxivid               | arXiv:1108.0669         | finds a specific record using its arXiv id
arXiv Class | arxiv_class:arxivclass       | arxiv_class:"High Energy Physics - Experiment" | finds all arXiv pre-prints in the class specified
Author       | author:"Last, F"            | author:"huchra, j"      | author name may include just lastname and initial
Author (cont.)| author:"Last, First [...]"  | author:"huchra, john p" | an example of stricter author search (recommended)
Bibcode      | bibcode:adsbib              | bibcode:2003AJ....125..525J | finds a specific record using the [ADS bibcode]({{ site.baseurl }}/help/actions/bibcode)
Bibliographic groups | bibgroup:name       | bibgroup:HST            | limit search to papers in HST bibliography (*)
Bibliographic stem | bibstem:adsbibstem    | bibstem:ApJ             | find records that contain a specific bibstem in their bibcode
Body         | body:"phrase"               | body:"gravitational waves" | search for a word or phrase in (only) the full text
Citation count | citation_count:count      | citation_count:40       | find records that have a specific number of citations
Copyright | copyright:copyright            | copyright:2012          | search for articles with certain copyrights
Data links   | data:archive                | data:NED                | limit search to papers with data from NED (*)
Database     | database:DB                 | database:astronomy      | limit search to either astronomy or physics or general
Date Range   | pubdate:[YYYY-MM TO YYYY-MM] | pubdate:[2005-10 TO 2006-09] | use fine-grained dates for publication range
Document type | doctype:type               | doctype:catalog         | limit search to records corresponding to data catalogs (*)
DOI          | doi:DOI                     | doi:10.1086/345794      | finds a specific record using its digital object id
First Author | author:"^Last, F"           | author:"^huchra, j"     | limit the search to first-author papers
Fulltext     | full:"phrase"               | full:"gravitational waves" | search for word or phrase in fulltext, acknowledgements, abstract, title and keywords
Grant        | grant:grant                 | grant:NASA              | finds papers with specific grants listed in them
Identifiers  | identifier:bibcode          | identifier:2003AJ....125..525J | finds a paper using any of its identifiers, arXiv, bibcode, doi, etc.
Issue        | issue:number                | issue:10                | search for papers in a certain issue
Keywords     | keyword:"phrase"            | keyword:sun             | search publisher- or author-supplied keywords
Language     | lang:"language"             | lang:korean             | search for papers with a given language
Object       | object:"object"             | object:Andromeda        | search for papers tagged with astronomical object by SIMBAD
ORCiD iDs    | orcid:id                    | orcid:0000-0000-0000-0000 | search for papers that are associated with a specific ORCiD iD
ORCiD iDs from publishers    | orcid_pub:id                    | orcid_pub:0000-0000-0000-0000 | search for papers that are associated with a specific ORCiD iD specified by a Publisher
ORCiD iDs from known ADS users    | orcid_user:id                    | orcid_id:0000-0000-0000-0000 | search for papers that are associated with a specific ORCiD iD claimed by known ADS users
ORCiD iDs from uknknown ADS users   | orcid_other:id                    | orcid_other:0000-0000-0000-0000 | search for papers that are associated with a specific ORCiD iD claimed by unknown ADS users
Page         | page:number                 | page:410                | search for papers with a given page number
Publication  | bibstem:"abbrev"            | bibstem:ApJ             | limit search to a <a href="http://adsabs.harvard.edu/abs_doc/journal_abbr.html" target="_blank">specific publication</a>
Properties   | property:type               | property:openaccess     | limit search to article with specific attributes (*)
Read count   | read_count:count            | read_count:10           | search for papers with a given number of reads
Title        | title:"phrase"              | title:"weak lensing"    | search for word or phrase in title field
VizieR keywords | vizier:"phrase"          | vizier:"Optical"        | search for papers with a given set of VizieR keywords
Volume       | volume:volume               | volume:10               | search for papers with a given volume
Year         | year:YYYY                   | year:2000               | require specific publication year
Year Range   | year:YYYY-YYYY              | year:2000-2005          | require publication date range

(*) See below for details on these filters.  In most cases, filtering of results based on these fields is available in the user interface.

### Properties

The "properties" search field allows one to restrict the search results to papers which belong to a particular class.  The allowed properties currently include:

Property flag    | Selection
---------------- | ------------------------
refereed         | refereed papers only
notrefereed      | non-refereed papers only
article          | records corresponding to regular articles
nonarticle       | not regular articles, for instance meeting abstracts, observing proposals, catalog descriptions, etc
ads_openaccess   | OA version of article is available from ADS
eprint_openaccess | OA version of article is available from arXiv
pub_openaccess   | OA version of article is available from publisher
openaccess       | article has at least one openaccess version available
ocrabstract      | records with an abstract generated from OCR (may contain typos or mistakes)

### Bibliographic Groups

The "bibgroup" search field allows restriction of the search results to one of the [ADS bibliographic groups](http://doc.adsabs.harvard.edu/abs_doc/help_pages/search.html#Select_References_From_Group).  These groups are curated by a number of librarians and archivists who maintain either institutional or "telescope" bibliographies on behalf of their projects.  Here is a partial list.  For more information on the criteria behind the curation of these groups, please see the link above.

The list of current Institutional bibgroups is: ARI, CfA, CFHT, Leiden, USNO

The list of current Telescope bibgroups is: ALMA, CXC, ESO, Gemini, Herschel, HST, ISO, IUE, JCMT, Keck, Magellan, NOAO, NRAO, ROSAT, SDO, SMA, Spitzer, Subaru, Swift, UKIRT, XMM

### Data Links

The "data" search field can be used to select papers which have data links associated to them.  The list of archives which ADS links to can be seen under the "Data" filter selection.  To generate a list of all records which have data links one can issue a simple wildcard query: [data:* ](https://ui.adsabs.harvard.edu/#search/q=data%3A*&sort=date+desc).  Using the data search field allows one to focus on data-rich papers, for example:

    data:(CXO OR XMM) AND data:HST

Finds multi-wavelength papers which have observations both in the X-ray spectrum (from Chandra or XMM) and in the optical (HST).  Of course additional search terms can be used to further refine the selection criteria.

### Document Type

Records in ADS are assigned a document type which is indexed in the "doctype" search field, the contents of which are an extension of the [BibTeX](https://en.wikipedia.org/wiki/BibTeX) entry types.  Currently these are the document types indexed by ADS:

Document Type  | Resource associated with record
---------------|--------------------------------
article        | journal article
eprint         | article preprinted in arXiv
inproceedings  | article appearing in a conference proceedings
inbook         | article appearing in a book
abstract       | meeting abstract
book           | book (monograph)
catalog        | data catalog (or other high-level data product)
circular       | printed or electronic circular
intechreport   | article appearing in a technical report
mastersthesis  | Masters thesis
newsletter     | printed or electronic newsletter
phdthesis      | PhD thesis
pressrelease   | press release
proceedings    | conference proceedings book
proposal       | observing or funding proposal
software       | software package
talk           | research talk given at a scholarly venue
techreport     | technical report
misc           | anything not found in the above list
