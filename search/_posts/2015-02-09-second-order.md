---
layout: post
title: "Smart Searches (Second Order Queries)"
order: 3
---



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

