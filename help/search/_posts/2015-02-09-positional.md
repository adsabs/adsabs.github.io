---
layout: post
title: "Positional Field Searches"
order: 4
---


The _pos()_ operator allows you to search for an item within a field by specifying the position in the field.  The syntax for this operator is _pos(fieldedquery,position,[endposition])_.  If no _endposition_ is given, then it is assumed to be _endposition = position_, otherwise this performs a query within the range _[position, endposition]_ where _position_ is the leftmost position considered and _endposition_ is the rightmost. For example:

Example                       | Results
------------------------------|--------------------------------
pos(author:"Oort, J",2)       | papers that have "J. Oort" as the second author
pos(author:"Oort, J",2,2)     | same as above
pos(author:"Oort, J",1,3)     | papers that have "J. Oort" as first, second, or third author
pos(author:"Oort, J",-1)      | papers that have "J. Oort" as the last author, could be only author
pos(author:"Oort, J",-2,-1)   | papers that have "J. Oort" as either of the last two authors
pos(aff:harvard,1)            | papers for which the first author has a Harvard affiliation
pos(title:M31,1)              | papers for which the title starts with "M31"

Currently the _pos()_ operator works on these fields: _author_, _aff_, _title_.

<!---###Truncation of result list###

You can limit the number of results returned by your search by using the _topn()_ operator, which accepts the syntax _topn(N,query)_ and returns the top N papers from a list of results

    topn(20,"galaxy clusters")

This will limit the list of results to be the 20 most relevant papers on "galaxy clusters." --->
