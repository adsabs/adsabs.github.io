---
layout: post
title: "Search Syntax"
order: 1
no-header: true
---


*One-box search bar:*
<img src="{{site.baseurl}}/img/one-box-search.png"  alt="" style="max-width:100%;display:block;margin-bottom:15px;">

## Search Basics

Our new one box search allows you to quickly formulate a query without having to enter data into multiple form fields, as you would in ADS Classic.
At a minimum, to use it successfully you will want to know the following:

* to search for an *author*, write **author:&ldquo;huchra,j"**
* to search for *multiple authors*, write **author:("huchra,j" "geller,m")**
* to search for a *first author*, write **author:&ldquo;^huchra,j"**

* to search for a *year or year range*, write **year:1995** or **year:1995-2000**
* to search for a *phrase*, enclose it in quotations: **"primordial black holes"**


## Fielded Searches

*FIELD* : [*QUERY*]

The list of searches shown above were examples of fielded searches. Fielded searches ensure that the correct database fields are queried for your results. Queries without fields will search in the article metadata and the full-text, which might return irrelevant results. For instance, if you are searching for papers by the author Marc Mars, you want to search for author:"Mars, M" in order to make sure you don't return papers that simply have the word "Mars" somewhere in the fulltext.  

Some more example searches:

 * "dark matter" -LHC
 * title:"QSO" year:1995-2000
 * arXiv:1012.5859
 * doi:10.1086/345794
 * bibcode:2003AJ....125..525J


###Available Fields

Field Name   | Search Field Syntax         | Example                 | Notes
------------ | --------------------------- | ----------------------- | -------------- 
Author       | author:"Last, F"            | author:"huchra, j"      | author name may include just lastname and initial 
Author (cont.)| author:"Last, First [...]"  | author:"huchra, john p" | an example of stricter author search (recommended) 
First Author | author:"^Last, F"           | author:"^huchra, j"     | limit the search to first-author papers    
Abstract     | abs:"phrase"                | abs:"dark energy"       | search for word or phrase in abstract      
Year         | year:YYYY                   | year:2000               | require specific publication year          
Year Range  | year:XXXX-YYYY              | year:2000-2005          | require publication date range             
Publication  | bibstem:"abbrev"            | bibstem:ApJ             | limit search to a <a href="http://adsabs.harvard.edu/abs_doc/journal_abbr.html">specific publication</a> 
Fulltext     | full:"phrase"               | full:"gravitational waves" | search for word or phrase in fulltext   
Bibcode      | bibcode:adsbib              | bibcode:2003AJ....125..525J | finds a specific record using the <A HREF="http://adsabs.harvard.edu/abs_doc/help_pages/data.html#bibcodes">ADS bibcode</A> 
arXiv ID     | arXiv:arxivid               | arXiv:1108.0669         | finds a specific record using its arXiv id
DOI          | doi:DOI                     | doi:10.1086/345794      | finds a specific record using its digital object id 
Affiliation  | aff:"phrase"                | aff:"harvard"           | search for word or phrase in affiliation field 
Title        | title:"phrase"              | title:"weak lensing"    | search for word or phrase in title field   
Keywords     | keyword:"phrase"            | keyword:sun             | search publisher- or author-supplied keywords 
Database     | database:DB                 | database:astronomy      | limit search to either astronomy or physics 
Properties   | property:type               | property:openaccess     | limit search to article with specific attributes (see below) 


##Combining Search Terms to Make a Compound Query

You can string together any of the search terms to develop a query.  By default search terms will be combined using AND as the default boolean operator, but this can be changed by explicitly specifying OR beween them.  Similarly one can exclude a term by prepending a "-" sign to it.  Multiple search words or phrases may be grouped in a fielded query by enclosing them in parenthesis.  Some examples:

    abs:(QSO "dark energy")                 # finds papers containing both "QSO" and "dark energy" in their abstract
    abs:(QSO OR "dark energy")              # finds papers containing either "QSO" or "dark energy in their abstract
    author:"huchra, j" -title:2mass         # finds papers by "J. Huchra" but excludes ones with "2mass" in their title
    
[See more examples.](examples.md#stringing-together-a-query)


## Querying for Properties (refereed, openaccess, etc)

The "properties" search field allows one to restrict the search results to papers which possess a particular property.  The allowed properties currently include:

Property flag  | Selection                
-------------- | ------------------------ 
refereed       | refereed papers only    
eprint         | arXiv eprints            
catalog        | astronomical catalogs (e.g. Vizier)          
openaccess     | there is at least one open access version of the article available   
software       | records for software packages (mostly from the [ASCL](http://ascl.net)) 

