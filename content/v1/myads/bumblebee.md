---
title: MyADS Bumblebee | ADS API
---

# MyADS Server Side Layer for Bumblebee

## Get Bumblebee Settings

Retrive various configuration options for the Bumblebee client.

	GET /vault/configuration/:key

### Scopes and limits
 * 100 req/day

Name | Type | Description
-----|------|--------------
`key`|`string` | Optional. Denotes the key that should be returned from the configuration. Default is to return everything.



<%= headers 200 %>
```json
{
    "link_servers": [
        {
            "gif": "http://sfx.brown.edu:8888/sfx_local/sfx.gif",
            "link": "http://sfx.brown.edu:8888/sfx_local",
            "name": "Brown University Library"
        },
        {
            "gif": "http://sfx.caltech.edu:8088/images/sfx.gif",
            "link": "http://sfx.caltech.edu:8088/caltech",
            "name": "California Institute of Technology"
        },
        {
            "gif": "http://elibrary.cf.ac.uk/sfx/img/azlist_ver3/cardiffsfx.gif",
            "link": "http://elibrary.cf.ac.uk/sfx",
            "name": "Cardiff University"
        }]
}
```

Example trying to access non-existing key

<%= headers 404 %>
```json
{}
```
