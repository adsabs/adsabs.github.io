---
layout: post
title: "Search Syntax"
order: 1
---


### Search Basics

ADS's one box search box utilizes fielded searches.  Queries without fields will search in the metadata and the full text, which may not return the results that you want.  For instance, if you are searching for papers by the author Marc Mars, you want to search for **author:"Mars, M"** instead of **Mars** to make sure that you don't return papers that simply have the word "Mars" somewhere in the article or metadata.  

### Preformatted Fielded Searches

Above the search box we supply shortcuts to 7 frequently used search fields.  Simply click on the field that you wish to search and enter your search term in provided format (generally between the supplied quotation marks.)  You may string several search terms together.  For instance if you want to find articles published between 1980 and 1990 which cite an article written by John Huchra, you can use the preformatted fields to generate the query below:

   citations(author:"Huchra, John") year:1980-1990

### Manually entering a fielded search

You can also enter the fields directly by prepending the field(s) that you wish to search to your search terms.  Unfielded searches may give you unwanted results.    

* to search for an *author*, enter **author:&ldquo;huchra,j"**
* to search for *multiple authors*, enter **author:("huchra,j" "geller,m")**
* to search for a *first author*, enter **author:&ldquo;^huchra,j"**
* to search for a *year or year range*, enter **year:1995** or **year:1995-2000**
* to search for a *phrase*, enclose it in quotations: **"primordial black holes"**
* to search for *citations* to a certain author, enter **citations(author:"huchra, j)**
* to search for *citations* to a certain article, enter **citations(1989Sci...246..897G)**



### Available Fields
This is a list of fields currently available in the ADS and the preferred search format.  

Field Name   | Search Field Syntax         | Example                 | Notes
------------ | --------------------------- | ----------------------- | --------------
Author       | author:"Last, F"            | author:"huchra, j"      | author name may include just lastname and initial
Author (cont.)| author:"Last, First [...]"  | author:"huchra, john p" | an example of stricter author search (recommended)
First Author | author:"^Last, F"           | author:"^huchra, j"     | limit the search to first-author papers    
Abstract     | abs:"phrase"                | abs:"dark energy"       | search for word or phrase in abstract      
Year         | year:YYYY                   | year:2000               | require specific publication year          
Year Range   | year:YYYY-YYYY              | year:2000-2005          | require publication date range             
Publication  | bibstem:"abbrev"            | bibstem:ApJ             | limit search to a <a href="http://adsabs.harvard.edu/abs_doc/journal_abbr.html" target="_blank">specific publication</a>
Fulltext     | full:"phrase"               | full:"gravitational waves" | search for word or phrase in fulltext   
Bibcode      | bibcode:adsbib              | bibcode:2003AJ....125..525J | finds a specific record using the [ADS bibcode]({{ site.baseurl }}/actions/bibcode)
arXiv ID     | arXiv:arxivid               | arXiv:1108.0669         | finds a specific record using its arXiv id
DOI          | doi:DOI                     | doi:10.1086/345794      | finds a specific record using its digital object id
Affiliation  | aff:"phrase"                | aff:"harvard"           | search for word or phrase in affiliation field
Title        | title:"phrase"              | title:"weak lensing"    | search for word or phrase in title field   
Keywords     | keyword:"phrase"            | keyword:sun             | search publisher- or author-supplied keywords
Database     | database:DB                 | database:astronomy      | limit search to either astronomy or physics or general
Properties   | property:type               | property:openaccess     | limit search to article with specific attributes [see below.] (Querying for Properties.md)


### Combining Search Terms to Make a Compound Query

You can string together any of the search terms to develop a query.  By default search terms will be combined using AND as the default boolean operator, but this can be changed by explicitly specifying OR beween them.  Similarly one can exclude a term by prepending a "-" sign to it.  Multiple search words or phrases may be grouped in a fielded query by enclosing them in parenthesis.  Some examples:

    abs:(QSO "dark energy")                 # finds papers containing both "QSO" and "dark energy" in their abstract
    abs:(QSO OR "dark energy")              # finds papers containing either "QSO" or "dark energy in their abstract
    author:"huchra, j" -title:2mass         # finds papers by "J. Huchra" but excludes ones with "2mass" in their title


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
