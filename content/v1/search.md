---
title: Search API | ADS API
---


# Search API

{:toc}



## Search for Documents

    GET /search/query?q=value&fl=value2.....

Query the search engine and return results. All parameters have to be properly url-encoded UTF-8. The response body will always be json encoded.


### Parameters

Name | Type | Description
-----|------|--------------
`q`|`string` | Query as described in [Query Syntax](qlanguage)
`fq`|`string`| Filter your query results using a particular `field:value` condition. This parameter is repeatable.
`fl`|`string`| Comma delimited list of fields to return. Default is `id` - see [List of Fields](fields)
`start`|`number`| For pagination, offset of the first returned result (default=0)
`rows`|`number`| How many records to return for this request (default=10, maximum=200)
`sort`|`string`| Indicate how you wish the result set sorted. The format is `field direction` where `direction` is one of `asc` or `desc`, and `field` is any of the valid indexes. The default sorting is by relevance (computed by our search engine). Example: `sort=read_count+desc` <br/> Some useful fields to sort by may be `pubdate`, `citation_count`, or `num_readers`.



<%= headers 200 %>
```json
    {
      "bibcode": "2012A&A...542A..16R",
      "author": [
        "Ranalli, P.",
        "Comastri, A.",
        ...
      ],
      "pub": "Astronomy and Astrophysics",
      "identifier": [
        "2012arXiv1204.4485R",
        "arXiv:1204.4485",
        "2012A&A...542A..16R"
      ],
      "title": "X-ray properties of radio-selected star forming galaxies in the Chandra-COSMOS survey",
      "property": [
        "REFEREED",
        "ARTICLE"
      ],
      "abstract": "X-ray surveys contain sizable numbers of star forming galaxies, ..."
      "keyword": [
        "astronomy x rays",
        "astronomy radio",
        "galaxies fundamental parameters",
        "galaxies star clusters",
        "galaxies active",
        ...
      ],
      "aff": [
        "Università di Bologna, Dipartimento di Astronomia, via Ranzani 1, 40127, Bologna, Italy ; Institute of Astronomy and Astrophysics, National Observatory of Athens, Palaia Penteli, 15236, Athens, Greece; INAF - Osservatorio Astronomico di Bologna, via Ranzani 1, 40127, Bologna, Italy",
        "INAF - Osservatorio Astronomico di Bologna, via Ranzani 1, 40127, Bologna, Italy",
        ...
      ],
    }
```


#### Example Search Requests


Query | Explanation
------|-------------------------------------------------
 `q=bibcode:2011ApJ...737..103S` |  Search by bibcode
 `q=black+holes&fq=database:astronomy` |  Search for "black holes", restricted to astronomy content
 `q=dark+energy&fq=author:"Civano,+F"&sort=citation_count+desc` |  Search for "dark energy", filter by author, sort by citation count
`q=dark+energy&sort=citation_count+desc&fl=bibcode,property` |   Return *bibcode* and *property* values
`q=author:"Kurtz,+M"&fq=property:refereed`|   Limit a search to only refereed articles
`q=transiting+exoplanets&rows=200`|  Search for "transiting exoplanets", get 200 rows
`q=transiting+exoplanets&rows=200&start=201`|   Same search but get the next 200 rows

 

## Parse a Query

    GET /search/qtree?q=:value

Returns a `query tree` (Abstract Syntax Tree - AST) as understood by our query parser. The structure can be used by external applications to eg:
rewrite the query or check its syntactic correctnes.

### Parameters

Name | Type | Description
-----|------|--------------
`q`  | string | Query as described in [Query Syntax](qlanguage)


<%= headers 200 %>
```json
{
             "qtree": "\n{\"name\":\"OPERATOR\", \"label\":\"DEFOP\", \"children\": [\n    {\"name\":\"MODIFIER\", \"label\":\"MODIFIER\", \"children\": [\n        {\"name\":\"TMODIFIER\", \"label\":\"TMODIFIER\", \"children\": [\n            {\"name\":\"FIELD\", \"label\":\"FIELD\", \"children\": [\n                {\"name\":\"QNORMAL\", \"label\":\"QNORMAL\", \"children\": [\n                    {\"name\":\"TERM_NORMAL\", \"input\":\"star\", \"start\":0, \"end\":3}]\n                }]\n            }]\n        }]\n    }]\n}",
             "responseHeader": {
              "status": 0,
              "QTime": 6,
              "params": {
               "q": "star",
               "wt": "json",
               "fl": "id"
              }
             }
            }
```            


## BigQuery

    POST /search/bigquery

Returns standard search results, but accepts as input very large query (i.e. a query that can be expressed only as a list of search
criteria, typically IDs). There is currently no limit to the size of the submitted data (besides buffer/time limits imposed by our API
frontend), however there are severe limits on how often you can call this enpoint. Typically, only 100 requests per day are allowed.

The `bigquery` is always executed as a filter **after** the main query (to filter out unwanted results and keep only the results
specified by the `bigquery`). You may want to use `q=*:*` to filter contents of the whole database, however it is advisable to make
the `q` as specific as possible. Broad queries have higher `qTime` (execution time) and that will be counted towards your rate-limit
(in the future).


The bigquery filter is *applied only after* the main search (ie: it limits results of the main search).

### Parameters

Name          | Type   | Description
--------------|--------|--------------
`query parameters`   |`ref`| See [Search Parameters above](#search-for-documents). <br/> **NOTE**: `q` should always be present, if `fq` is missing we'll set the default `fq={!bitset}`. In most situations this works, but in rare circumstances you may want to specify it (ie: when you want to use multiple `fq` queries).
`filestream`     |`string`| **Required**. Newline separated list of values, the first line specifies the index field, the rest are the search values. <br/> Currently, we allow to search in `bibcode` index only. You can submit `canonical` as well as `alternate` bibcodes - the search will automatically match both. In the future, the list of available indexes may be extended).


### Headers

Name          | Type   | Description
--------------|--------|--------------
`Content-Type`|`string`| Optional. Default is `big-query/csv`, it influences the way how the values from the `filestream` parameter are parsed. In the future ADS may support `json` and some other formats. 


Example python session - get all papers from ADS and filter them using several IDs:

```python
import requests
bibcodes="bibcode\n1907AN....174...59.\n1908PA.....16..445.\n1989LNP...334..242S"
r = requests.post('https://api.adsabs.harvard.edu/v1/search/bigquery', 
       params={'q':'*:*', 'wt':'json', 'fq':'{!bitset}', 'fl':'bibcode'}, 
       headers={'Authorization': 'Bearer: TOKEN'},
       data=bibcodes)
```

<%= headers 200 %>
<%= json(:issue_search_results) %>


## Source Code

The source code of the microservice is accessible at https://github.com/adsabs/solr-service.

The source code of the search engine is accessible at https://github.com/romanchyla/montysolr.
  


