---
layout: post
title: "Positional Field Searches"
order: 4
---


The _pos()_ operator allows you to search for an item within a field by specifying the position in the field.  The syntax for this operator is _pos(fieldedquery,position)_ For example:

    pos(author:"Oort, J",2)         # returns papers which have "J. Oort" as the second author
    pos(aff:harvard,1)              # returns papers for which the first author has a Harvard affiliation
    pos(title:M31,1)                # returns papers for which the title start with "M31"
    
Currently the _pos()_ operator works on these fields: _author_, _aff_, _title_.

<!---###Truncation of result list###

You can limit the number of results returned by your search by using the _topn()_ operator, which accepts the syntax _topn(N,query)_ and returns the top N papers from a list of results

    topn(20,"galaxy clusters")
    
This will limit the list of results to be the 20 most relevant papers on "galaxy clusters." --->
