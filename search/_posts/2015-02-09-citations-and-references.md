---
layout: post
title: "Citation and Reference Operators"
order: 2
---



The search engine supports two operators which generate lists of references or citations from a query.  The syntax for this operators are _references(query)_ and _citations(query)_.  Some examples will help clarify their use:

    citations(author:"huchra, john")           # returns the list of papers citing John Huchra's papers
    references(bibcode:2003AJ....125..525J)    # returns papers cited by the paper 2003AJ....125..525J
    citations(abs:HST)                         # returns papers citing papers which have "HST" in their abstract
    
One powerful aspect of having these operators at our disposal when creating a query is that we can combine them with additional search terms to expand or narrow your query.  For example, the following query finds all papers which cite [the original JWST paper](http://labs.adsabs.harvard.edu/adsabs/abs/2006SSRv..123..485G/) as well as papers which contain the terms "Webb" or "JWST" in their abstract:

    citations(bibcode:2006SSRv..123..485G) OR abs:(Webb OR JWST)