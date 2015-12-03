---
title: MyADS | ADS API
---

# MyADS API

{:toc}

MyADS is a microservice for storing user-related information.


## Save a Query

Queries can be saved for later execution (or simply as a part of user history).

	POST /vault/query

### Scopes
 * **store-query**

### Parameters

Name | Type | Description
-----|------|--------------
`query parameters`|`ref` | Query parameters, see [Search Syntax Documentation](search/qlanguage) and [Search API](search)
`bigquery`|`string`| Optional. A BigQuery filter, see [BigQuery Documentation](search#bigquery)
`


``` command-line
$ curl 'https://api.adsabs.harvard.edu/v1/vault/query' -H 'Authorization: Bearer:TOKEN' -X POST -d $'{"q":"*:*15IAUGA..2257982A\\n2015IAUGA..2257768A\\n2015IAUGA..2257639R\\n2015ASPC..492..208G\\n2015ASPC..492..204F\\n2015ASPC..492..189A\\n2015ASPC..492..150T\\n2015ASPC..492...85E\\n2015ASPC..492...80H\\n2015AAS...22533656H"}' -H 'Content-Type: application/json'

> {"qid": "dcd173130bbbbb957eafd866baf38b2c", "numFound": 9}
```


## Get Query Info

Retrive information about the previously stored query.

	GET /vault/query/:query_id

### Scopes
 * **store-query**

### Parameters

Name | Type | Description
-----|------|--------------
`query_id`|`string` | Query ID that was returned by `POST /query`

<%= headers 200 %>
```json
{
    "numfound": 9,
    "qid": "dcd173130bbbbb957eafd866baf38b2c",
    "query": "{\"query\": \"fq=%7B%21bitset%7D&q=%2A%3A%2A\", \"bigquery\": \"bibcode\\n15ASPC..495..40015IAUGA..2257982A\\n2015IAUGA..2257768A\\n2015IAUGA..2257639R\\n2015ASPC..492..208G\\n2015ASPC..492..204F\\n2015ASPC..492..189A\\n2015ASPC..492..150T\\n2015ASPC..492...85E\\n2015ASPC..492...80H\\n2015AAS...22533656H\"}"
}
```

## Execute Saved Query

Search using the stored query and return the same data as [Search API](search) endpoint.

	GET /vault/execute_query/:query_id

### Scopes and Ratelimits
 * **execute-query**
 * 100 reqs/day

### Parameters

Name | Type | Description
-----|------|--------------
`query parameters`|`ref` | Optional. You can submit query parameters that override parts of the saved query. Query parameters, see [Search Syntax Documentation](search/qlanguage) and [Search API](search)

<%= headers 200 %>
```json
{
    "response": {
        "docs": [
            {
                "id": "10690723"
            },
            {
                "id": "11057363"
            },
            {
                "id": "10564749"
            },
            {
                "id": "10796089"
            },
            {
                "id": "10867252"
            },
            {
                "id": "10867221"
            },
            {
                "id": "10867251"
            },
            {
                "id": "10867277"
            },
            {
                "id": "11057812"
            }
        ],
        "numFound": 9,
        "start": 0
    },
    "responseHeader": {
        "QTime": 6,
        "params": {
            "fl": "id",
            "fq": "{!bitset}",
            "q": "*:*",
            "wt": "json"
        },
        "status": 0
    }
}
```

## Save User Data

Endpoint for saving user preferences. Used mostly by BumbleBee client.

	POST /vault/user-data

### Scopes and limits
 * **store-preferences**
 * 100 reqs/day

### Parameters

Name | Type | Description
-----|------|--------------
`JSON payload`|`JSON` | JSON object, to be stored for the user. **WARNING**: the JSON will replace the existing one. If you send an empty POST request, the stored data will be replaced with `{}`.



``` command-line
$ curl -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" "https://api.adsabs.harvard.edu/v1/vault/user-data" -X POST -d $'{"foo": "bar"}'
> {"foo": "bar"}
```

## Get User Preferences

Retrive stored preferences.

	GET /vault/user-data

### Scopes and limits
 * **store-preferences**
 * 100 req/day


<%= headers 200 %>
```json
{"foo": "bar"}
```

## Source Code

The source code of the microservice is available at: https://github.com/adsabs/myads
