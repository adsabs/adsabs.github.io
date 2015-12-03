---
title: Orcid | ADS API
---

{:toc}


# ORCiD API

ORCID is a service provided by http://orcid.org. It allows researchers register their 
works in a central repository.

ADS has created [ORCiD integration](https://github.com/adsabs/bumblebee/tree/master/src/js/modules/orcid) which
is used by the visitors of the [ADS website](https://ui.adsabs.harvard.edu) to claim/curate their works in ORCiD.

## Getting ORCiD Profiles

Check with ORCiD and downloads the fresh profile from the ORCiD API. We can return the orcid profile only if
a user ever logged in with ADS (and also the OAuth `access_token` is stil valid).

	GET /get-profile/:orcid_id

### Scopes

 * **ads-consumer:orcid**

### Parameters

Name | Type | Description
-----|------|--------------
`orcid_id`  | `string` | ORCiD ID


<%= headers 200 %>
```json

{
    "error-desc": null,
    "message-version": "1.2",
    "orcid-profile": {
        "client-type": null,
        "group-type": null,
        "orcid": null,
        "orcid-activities": {
            "affiliations": null,
            "funding-list": null,
            "orcid-works": {
                "orcid-work": [
                    {
                        "country": null,
                        "created-date": {
                            "value": 1446830582917
                        },
                        "journal-title": null,
                        "language-code": null,
                        "last-modified-date": {
                            "value": 1446830582917
                        },
                        "publication-date": {
                            "day": null,
                            "media-type": null,
                            "month": {
                                "value": "08"
                            },
                            "year": {
                                "value": "2015"
                            }
                        },
                        "put-code": "20054210",
                        "short-description": "Whether or not scholarly publications are going through an evolution or revolution, one comforting certainty remains: the NASA Astrophysics Data System (ADS) is here to help the working astronomer and librarian navigate through the increasingly complex communication environment we find ourselves in. Born as a bibliographic database, today's ADS is best described as a an \"aggregator\" of scholarly resources relevant to the needs of researchers in astronomy and physics. In addition to indexing content from a variety of publishers, data and software archives, the ADS enriches its records by text-mining and indexing the full-text articles, enriching its metadata through the extraction of citations and acknowledgments and the ingest of bibliographies and data links maintained by astronomy institutions and data archives. In addition, ADS generates and maintains citation and co-readership networks to support discovery and bibliometric analysis.In this talk I will summarize new and ongoing curation activities and technology developments of the ADS in the face of the ever-changing world of scholarly publishing and the trends in information-sharing behavior of astronomers. Recent curation efforts include the indexing of non-standard scholarly content (such as software packages, IVOA documents and standards, and NASA award proposals); the indexing of additional content (full-text of articles, acknowledgments, affiliations, ORCID ids); and enhanced support for bibliographic groups and data links. Recent technology developments include a new Application Programming Interface which provides access to a variety of ADS microservices, a new user interface featuring a variety of visualizations and bibliometric analysis, and integration with ORCID services to support paper claiming.",
                        "source": {
                            "source-client-id": {
                                "host": "orcid.org",
                                "path": "APP-BA5POB6F5D7CTHX2",
                                "uri": "http://orcid.org/client/APP-BA5POB6F5D7CTHX2",
                                "value": null
                            },
                            "source-date": {
                                "value": 1446830582917
                            },
                            "source-name": {
                                "value": "NASA ADS"
                            },
                            "source-orcid": null
                        },
 # output truncated ....


```

If the user revoked their OAuth token:

<%= headers 404 %>
```json
{
 "error" : "We do not have access_token for: 0000-0000-0000-0000"
}
```

If the ORCiD ID is not known to us:

<%= headers 404 %>
```json
{
 "error" : "We do not have a record for: 0000-0000-0000-0000"
}
```


## Getting Recent Updates

Return information about users who recently updated their ORCiD information through Bumblebee (ADS UI). This includes also users who just accessed their ORCiD profiles, even if they didn't make new claims. This enpoint always returns maximum of 10 records created since (inclusive) the requested date. To access the next records, use the `updated` date + 1 additional microsecond.


	GET /export/:iso_datestring

### Scopes

 * **ads-consumer:orcid**

### Parameters

Name | Type | Description
-----|------|--------------
`iso_datestring`  | `string` | Date in ISO format (RFC3339, UTC time zone, ie. '2008-09-03T20:56:35.450686Z')
`fields`|`list`| Optional. List of fields to return in response, allowed values are: `orcid_id`, `created`, `updated`, `profile`, `info`

<%= headers 200 %>
```json
[
    {
        "created": "2015-11-15T17:46:28.657982",
        "orcid_id": "0000-0002-9384-846X",
        "updated": "2015-11-15T20:58:27.656195",
        "info": {},
        "profile": {
            "error-desc": null,
            "message-version": "1.2",
            "orcid-profile": {
                "client-type": null,
                "group-type": null,
                "orcid": null,
                "orcid-activities": {
                    "affiliations": {
                        "affiliation": [
                            {
                                "created-date": {
                                    "value": 1438088550409
                                },
                                "department-name": null,
                                "end-date": null,
                                "last-modified-date": {
                                    "value": 1438088550409
                                },
                                "organization": {
                                    "address": {
                                        "city": "Firenze",
                                        "country": "IT",
                                        "region": "Toscana"
                                    },
                                    "disambiguated-organization": {
                                        "disambiguated-organization-identifier": "56860",
                                        "disambiguation-source": "RINGGOLD"
                                    },
                                    "name": "Osservatorio Astrofisico di Arcetri"
                                },
                                "put-code": "1060794",
                                "role-title": "Researcher",
                                "source": {
                                    "source-client-id": null,
                                    "source-date": {
                                        "value": 1438088550409
                                    },
                                    "source-name": {
                                        "value": "Simone Bianchi"
                                    },
                                    "source-orcid": {
                                        "host": "orcid.org",
                                        "path": "0000-0002-9384-846X",
                                        "uri": "http://orcid.org/0000-0002-9384-846X",
                                        "value": null
                                    }
                                },
                   # output truncated
    },
    {
     ...
    }
]
```


## Source Code

The source code of this microservice is at https://github.com/adsabs/orcid-service.
