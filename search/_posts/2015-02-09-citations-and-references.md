---
layout: post
title: "Citation and Reference Operators"
order: 2
---

When you submit a query, ADS returns a list of search results. Should you want a list of all the articles which **cite those search results** , or all the articles which **are referenced by those search results**, you can use the citation or reference operators.

The syntax for these operators are _references(query)_ and _citations(query)_.

Examples:

    citations(author:"huchra, john")           # returns the list of papers citing John Huchra's papers
    references(bibcode:2003AJ....125..525J)    # returns papers cited by the paper 2003AJ....125..525J
    citations(abs:HST)                         # returns papers citing papers which have "HST" in their abstract
    
One powerful aspect of having these operators at our disposal when creating a query is that we can combine them with additional search terms to expand or narrow your query.  For example, the following query finds all papers which cite <a href="https://ui.adsabs.harvard.edu/#abs/2006SSRv..123..485G/abstract" target="_blank">the original JWST paper</a> as well as papers which contain the terms "Webb" or "JWST" in their abstract:

    citations(bibcode:2006SSRv..123..485G) OR abs:(Webb OR JWST)