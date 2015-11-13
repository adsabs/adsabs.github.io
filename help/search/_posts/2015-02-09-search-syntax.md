---
layout: post
title: "Search Syntax"
order: 1
---


### Search Basics

ADS's one box search box utilizes fielded searches.  Queries without fields will search in the metadata and the full text, which may not return the results that you want.  For instance, if you are searching for papers by the author Marc Mars, you want to search for **author:"Mars, M"** instead of **Mars** to make sure that you don't return papers that simply have the word "Mars" somewhere in the article or metadata.

### Fielded Searches

Above the search box we supply shortcuts to 5 frequently used search fields.  Simply click on the field that you wish to search and enter your search term in provided format (generally between the supplied quotation marks).  Alternatively, if you start entering the name of a field an autocomplete feature will suggest a list of fields.  You may string several search terms together.  For instance if you want to find articles published between 1980 and 1990 by John Huchra, you can use:

    **author:"Huchra, John" year:1980-1990**

Here is a list of search examples for commonly used fields:    

Example Query                        | Explanation
-------------------------------------|------------------------------------------------------------
author:"huchra, john"                | search for papers written by an author
author:"^huchra, john"               | limit search to first-author papers
abs:"dark energy"                    | search for the phrase "dark energy" in abstract and title
year:2000                            | search for publications written in 2000
year:2000-2005                       | search for publications written between 2000 and 2005 (inclusive)
full:"gravitational waves"           | search for papers containing the phrase "gravitational waves" anywhere in the full-text
bibstem:ApJ                          | select papers published in a particular publication

### Combining Search Terms to Make a Compound Query

You can string together any number of search terms to develop a query.  By default search terms will be combined using AND as the default boolean operator, but this can be changed by explicitly specifying OR beween them.  Similarly one can exclude a term by prepending a "-" sign to it (or using the boolean "NOT").  Multiple search words or phrases may be grouped in a fielded query by enclosing them in parenthesis.  Some examples:

Example Query                        | Results
-------------------------------------|--------------------------------------------------------------
abs:(QSO "dark energy")              | papers containing both "QSO" and "dark energy" in their abstract
abs:(QSO OR "dark energy")           | papers containing either "QSO" or "dark energy in their abstract
author:"huchra, j" -title:2mass      | papers by "J. Huchra" but excludes ones with "2mass" in their title
author:"huchra, j" NOT title:2mass   | same as above

### Synonyms and Acronyms

By default most search terms in ADS are expanded by adding a list of words which are synonyms of the search term.  So for example, a search of "star" in the title field will be expanded to include words such as "stars," "stellar," "starry," "starlike," and so on.  (Notice that this often includes words in foreign languages such as "etoile," "stern," and "stella"). While this feature improves recall, it sometimes compromises the precision of the results.  Our search engine allows one to turn off the synonym expansion feature by simply prepending an "=" sign in front of the search term.  

Our search engine also identifies acronyms during indexing and searching (defined as words consisting entirely of uppercase characters).  A search for an uppercase word will only match documents which contain that acronym, whereas a search for a lowercase word will match documents which contain any variation of the word, irregardless of its case.  Acronyms can themselves have synonyms (for example "ADS" and "Astrophysics Data System" are synonyms), so one should be aware that there is an interaction between case-sensitiveness and synonym expansion.  The examples below illustrate these effects:

Example Query                         | Results
--------------------------------------|-------------------------------------------------------------------
title:star                            | title contains "star", any of its synonyms, or the acronym "STAR"
title:etoile                          | title contains "star" or any of its synonyms (etoile being a synonym of star); no acronym ETOILE exists
=title:star                           | title contains "star" or the acronym "STAR"
=title:etoile                         | title contains "etoile"
title:STAR                            | title contains the acronym "STAR"
title:(=star NOT STAR)                | title contains "star" but not the acronym "STAR"
fuse                                  | the word "fuse" or acronym "FUSE" appear anywhere in the paper
FUSE                                  | the acronym "FUSE" appears anywhere in paper

### Author Searches

Synoym expansion also applies to author names, which provide a way to account for changes in a person's name and/or different spellings due to transliterations.  In addition to this, the default author search in ADS is "greedy" in the sense that it will retun all documents in which an author signature may match the input search string.  This allows, for instance, to have an author search for "Huchra, John" to return papers where the author name appears as "Huchra, John" or "Huchra, J."  By prepending the "=" character to the author search one can disable this feature (as well as any additional synonym expansion) and require an exact match on the author name.  Some examples:

Example Query                 | Results
------------------------------|---------------------------------------------------------------
author:"murray, s"            | Least precise variations: finds records authored by any of the following:<ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S.</li><li>Murray, S.</li><li>Murray, Stephen D.</li><li>Murray, S. D.</li><li>Murray, Sarah S.</li><li>Murray, Scott</li><li>...</li></ul>(any possible combination with last name "murray" and first name starting with S)
author:"murray, stephen"      | More precise variations: finds record authored by any of the following: <ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S.</li><li>Murray, S.</li><li>Murray, Stephen D.</li><li>Murray, S. D.</li><li>...</li></ul>(any possible variation of "Murray, Stephen" with or without middle name)
author:"murray, stephen s"    | Most precise variations: finds record authored by any of the following: <ul><li>Murray, Stephen S.</li><li>Murray, Stephen</li><li>Murray, S. S.</li><li>Murray, S.</li></ul>(any possible variation of "Murray, Stephen S" but no others)
=author:"murray, s"           | Matches only records authored by "Murray, S."
=author:"murray, stephen"     | Matches only records authored by "Murray, Stephen"
=author:"murray, stephen s"   | Matches only records authored by "Murray, Stephen S."

As a general rule we recommend to use the full name of the person for author searches since as can be seen above the matching rules in ADS are designed to find the maximal set of records consistent with the author specification given by the user.  Rather than disabling the name-variation algorithm described above, we recommend performing refinement of search results via the user interface filters for author names as described in the ["Filter your search" section]({{ site.baseurl }}/help/actions/filter)


### Available Fields
This is a list of fields currently available in the ADS and the preferred search format.  

Field Name   | Search Field Syntax         | Example                 | Notes
------------ | --------------------------- | ----------------------- | --------------
Author       | author:"Last, F"            | author:"huchra, j"      | author name may include just lastname and initial
Author (cont.)| author:"Last, First [...]"  | author:"huchra, john p" | an example of stricter author search (recommended)
First Author | author:"^Last, F"           | author:"^huchra, j"     | limit the search to first-author papers    
Abstract     | abs:"phrase"                | abs:"dark energy"       | search for word or phrase in abstract & title      
Year         | year:YYYY                   | year:2000               | require specific publication year          
Year Range   | year:YYYY-YYYY              | year:2000-2005          | require publication date range             
Publication  | bibstem:"abbrev"            | bibstem:ApJ             | limit search to a <a href="http://adsabs.harvard.edu/abs_doc/journal_abbr.html" target="_blank">specific publication</a>
Fulltext     | full:"phrase"               | full:"gravitational waves" | search for word or phrase in fulltext   
Bibcode      | bibcode:adsbib              | bibcode:2003AJ....125..525J | finds a specific record using the [ADS bibcode]({{ site.baseurl }}/help/actions/bibcode)
arXiv ID     | arXiv:arxivid               | arXiv:1108.0669         | finds a specific record using its arXiv id
DOI          | doi:DOI                     | doi:10.1086/345794      | finds a specific record using its digital object id
Affiliation  | aff:"phrase"                | aff:"harvard"           | search for word or phrase in affiliation field
Title        | title:"phrase"              | title:"weak lensing"    | search for word or phrase in title field   
Keywords     | keyword:"phrase"            | keyword:sun             | search publisher- or author-supplied keywords
Database     | database:DB                 | database:astronomy      | limit search to either astronomy or physics or general
Bibliographic group | bibgroup:name        | bibgroup:HST            | limit search to papers in HST bibliography
Properties   | property:type               | property:openaccess     | limit search to article with specific attributes (see below)


### Querying for Properties (refereed, openaccess, etc)

The "properties" search field allows one to restrict the search results to papers which possess a particular property.  The allowed properties currently include:

Property flag  | Selection                
-------------- | ------------------------
refereed       | refereed papers only   
notrefereed    | non-refereed papers only
eprint         | arXiv eprints            
nonarticle     | not regular articles, for instance meeting abstracts, observing proposals, catalog descriptions, etc
catalog        | astronomical catalogs (e.g. Vizier)
inproceedings  | papers which are in conference proceedings
inbook         | papers which are chapters in books
openaccess     | there is at least one open access version of the article available
ADS_openaccess | open access papers that have been scanned by the ADS
pub_openaccess | open access papers supplied by the publisher
software       | records for software packages (mostly from the <a href="http://ascl.net" target="_blank">ASCL</a>)
ocrabstract    | abstracts in ocr format
