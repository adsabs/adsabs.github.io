---
title: Search Syntax and the Query Language | ADS API
---

# Query Syntax

{:toc}


The search engine API uses similar syntax as [Apache Solr](http://lucene.apache.org/solr/). For a full reference of query possibilities, please refer to the Solr documentation and [ADS Search Help](http://adsabs.github.io/help/search/). The sections below present useful parameters and patterns for the vast majority of use cases, but are not meant to be exhaustive.

## Basic Rules


The `q` parameter supports both fielded and unfielded searching:

* `black holes`
* `title:black` `title:holes`

Use quotation marks to indicate phrase searching:
    
* `"black holes"`
* `title:"black holes"`

Prepend terms with "+" or "-" to indicate inclusion or exclusion:

* `+transiting exoplanets`
* `"dark energy" -"weak lensing"`

To filter by a publication date range you can use either the `year` or `pubdate` fields:
    
* `pubdate:[2013-07-00 TO *]`
* `pubdate:[2005-01 TO 2007-01]`
* `pubdate:2013-02`
* `year:2013`
* `year:[2012 TO 2013]`

The default search uses a boolean `AND` between terms, but you may use `OR` and `AND` in combination with `()` to create more complex queries.

Prefix queries (wildcards, `*`) are supported for most fields.

## Boolean Operators

TBD

## Analytical Functions

TBD

