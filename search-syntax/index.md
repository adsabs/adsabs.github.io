---
layout: page
title: Search the ADS
permalink: /search-syntax/
---


Our new one box search allows for you to search for a combination of author, title, year, or keywords.  By default the query terms will be searched for in the article metadata as well as the full-text contents.  To restrict the search to a particular field, simply prepend the field name to the term being searched for. Identifiers such as bibcodes, arXiv IDs and DOIs are recognized as well. 
Some example searches:

 * "weak lensing"
 * author:"huchra, j"
 * "dark matter" -LHC
 * title:"QSO" year:1995-2000
 * arXiv:1012.5859
 * doi:10.1086/345794
 * bibcode:2003AJ....125..525J
 
Unfielded searches may give more results than one would like since one would be searching the whole body of ADS records.  A fielded query will result in a better result list.  

Fielded searches can be made by prepending the search terms with the appropriate field keyword.  A list of the most common fields is displayed above the search box and clicking on each one of them will pre-generate the proper search syntax for you.  Here is the list as currently implemented:

Field Name   | Search Field Syntax         | Example                 | Notes                                      
------------ | --------------------------- | ----------------------- | ------------------------------------------ 
Author       | author:"Last, F"            | author:"huchra, j"      | author name may include just lastname and initial 
             | author:"Last, First [...]"  | author:"huchra, john p" | an example of stricter author search (recommended) 
First Author | author:"^Last, F"           | author:"^huchra, j"     | limit the search to first-author papers    
Abstract     | abs:"phrase"                | abs:"dark energy"       | search for word or phrase in abstract      
Year         | year:YYYY                   | year:2000               | require specific publication year          
             | year:XXXX-YYYY              | year:2000-2005          | require publication date range             
Publication  | bibstem:"abbrev"            | bibstem:ApJ             | limit search to a <a href="http://adsabs.harvard.edu/abs_doc/journal_abbr.html">specific publication</a> 
Fulltext     | full:"phrase"               | full:"gravitational waves" | search for word or phrase in fulltext   

You can string together any of the search terms to develop a query.  By default search terms will be combined using AND as the default boolean operator, but this can be changed by explicitly specifying OR beween them.  Similarly one can exclude a term by prepending a "-" sign to it.  Multiple search words or phrases may be grouped in a fielded query by enclosing them in parenthesis.  Some examples:

    abs:(QSO "dark energy")                 # finds papers containing both "QSO" and "dark energy" in their abstract
    abs:(QSO OR "dark energy")              # finds papers containing either "QSO" or "dark energy in their abstract
    author:"huchra, j" -title:2mass         # finds papers by "J. Huchra" but excludes ones with "2mass" in their title
    
[See more examples.](examples.md#stringing-together-a-query)

In addition to the search fields listed above, you may also use the following options to limit your search.  Please note that with exception of the bibcode not all fields are necessarily populated for all records.

Field Name   | Search Field Syntax         | Example                 | Notes                                      
------------ | --------------------------- | ----------------------- | ------------------------------------------
Bibcode      | bibcode:adsbib              | bibcode:2003AJ....125..525J | finds a specific record using the <A HREF="http://adsabs.harvard.edu/abs_doc/help_pages/data.html#bibcodes">ADS bibcode</A> 
arXiv ID     | arXiv:arxivid               | arXiv:1108.0669         | finds a specific record using its arXiv id
DOI          | doi:DOI                     | doi:10.1086/345794      | finds a specific record using its digital object id 
Affiliation  | aff:"phrase"                | aff:"harvard"           | search for word or phrase in affiliation field 
Title        | title:"phrase"              | title:"weak lensing"    | search for word or phrase in title field   
Keywords     | keyword:"phrase"            | keyword:sun             | search publisher- or author-supplied keywords 
Database     | database:DB                 | database:astronomy      | limit search to either astronomy or physics 
Properties   | property:type               | property:openaccess     | limit search to article with specific attributes (see below) 

The "properties" search field allows one to restrict the search results to papers which possess a particular property.  The allowed properties currently include:

Property flag  | Selection                
-------------- | ------------------------ 
refereed       | refereed papers only    
eprint         | arXiv eprints            
catalog        | astronomical catalogs (e.g. Vizier)          
openaccess     | there is at least one open access version of the article available   
software       | records for software packages (mostly from the [ASCL](http://ascl.net)) 

More options for selecting properties will become available soon.

The **"+ options"** button next to the search box allows you to  
  * specify a publication date range to search in between (if you do not know the month you may use "00".)  
  * disable fulltext (searches only article metadata and not the entire article)
  * select articles only (this excludes documents like observing proposals, catalog descriptions, meeting abstracts and communications)
  * specify which databases to be searched.  The default is set to search both the astronomy and physics databases but you can specify to search only the astronomy database or to search only the physics database or to search all databases (by selecting all you will include articles which have not been categorized as physics or astronomy, e.g. arXiv preprints in computer science or general science articles in journals.)  
  * specify how many results to display on one page (20 is the default; 3000 is the maximum.)
  
##Advanced Searches##

Our search engine supports a list of operators which can take any query and manipulate the list of results to accomplish additional functionality.

###Second-order Queries###

We provide three operators which modify the query results by performing second-order operations on the original query. To use them, simply click on one of the three options below the search box or wrap your query with the corresponding operator in the search box.

**Trending** -- returns the list of documents most read by users who read recent papers on the topic being researched; these are papers currently being read by people interested in this field.  For example:

    trending(exoplanets)
    
will return a ranked list of papers which are currently popular among the readers interested in exoplanets.

**Useful** -- returns the list of documents frequently cited by the most relevant papers on the topic being researched; these are studies which discuss methods and techniques useful to conduct research in this field.  For example:

    useful("galaxy surveys")

will return a ranked list of papers spanning a variety of topics useful to researchers interested in analyzing surveys of galaxies.

**Instructive** -- returns the list of documents citing the most relevant papers on the topic being researched; these are papers containing the most extensive reviews of the field.  For example:

    instructive("weak lensing")

will return a ranked list of papers featuring reviews of weak gravitational lensing and its cosmological implications. 

###Citation and Reference operators###

The search engine supports two operators which generate lists of references or citations from a query.  The syntax for this operators are _references(query)_ and _citations(query)_.  Some examples will help clarify their use:

    citations(author:"huchra, john")           # returns the list of papers citing John Huchra's papers
    references(bibcode:2003AJ....125..525J)    # returns papers cited by the paper 2003AJ....125..525J
    citations(abs:HST)                         # returns papers citing papers which have "HST" in their abstract
    
One powerful aspect of having these operators at our disposal when creating a query is that we can combine them with additional search terms to expand or narrow your query.  For example, the following query finds all papers which cite [the original JWST paper](http://labs.adsabs.harvard.edu/adsabs/abs/2006SSRv..123..485G/) as well as papers which contain the terms "Webb" or "JWST" in their abstract:

    citations(bibcode:2006SSRv..123..485G) OR abs:(Webb OR JWST)

###Positional Field Searches###

The _pos()_ operator allows you to search for an item within a field by specifying the position in the field.  The syntax for this operator is _pos(fieldedquery,position)_ For example:

    pos(author:"Oort, J",2)         # returns papers which have "J. Oort" as the second author
    pos(aff:harvard,1)              # returns papers for which the first author has a Harvard affiliation
    pos(title:M31,1)                # returns papers for which the title start with "M31"
    
Currently the _pos()_ operator works on these fields: _author_, _aff_, _title_.

###Truncation of result list###

You can limit the number of results returned by your search by using the _topn()_ operator, which accepts the syntax _topn(N,query)_ and returns the top N papers from a list of results

    topn(20,"galaxy clusters")
    
This will limit the list of results to be the 20 most relevant papers on "galaxy clusters."  
