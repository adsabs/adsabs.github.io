---
title: Orcid Editing | ADS API
---

{:toc}


# Editing ORCiD records with ADS

Some researchers may want to take advantage of the ADS 
to curate their records in an automated fashion (but typically, it will be only **their own** ORCiD profiles
since you need to have both the ADS and ORCiD OAuth tokens).

## Pre-requisites

When using this porting of ADS API, you are accessing user's resources as `NASA ADS` ORCiD client (APP-BA5POB6F5D7CTHX2). 

All the request (besides logging in) must contain the `Orcid-Authorization` header, plus the usual `Authorization` ie:

``` command-line

$ curl -H 'Authorization: Bearer:ADSTOKEN' -H 'Orcid-Authorization: Bearer:ORCIDTOKEN' https://api.adsabs.harvard.edu/v1/orcid/....
```

The `Orcid-Authorization` token is always tight to a specific ORCiD ID. Then endpoints follow the conventions of the ORCiD API. 
The ORCiD data is not modified in any ways (by our API).


## Documentation

All messages/communication must conform to the ORCiD schema. For further information see:

 * http://members.orcid.org/api
 * https://github.com/ORCID/ORCID-Source/blob/master/orcid-model/src/main/resources/README.md


Because the ORCiD documentation is rapidly evolving and it might be challenging to find explanation for some actions
we also recommend to observe the ADS integration with ORCiD in your browser.

 * go to https://ui.adsabs.harvard.edu/
 * open developer console in your browser
 * login with ORCID
 * claim some papers or display profile
 * observe the AJAX request that exhanged with the `/orcid` endpoint (some browsers will allow you to
   copy/paste the requests as CURL commands)

Also look at: https://github.com/adsabs/bumblebee/tree/master/src/js/modules/orcidd


## Accessing ORCiD Profile

	GET /:orcid_id/orcid-profile

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

	POST /:orcid_id/orcid-profile

This endpoint is used for updating author's ORCiD profile. The submitted payload has to be JSON
and formatted according to ORCiD message schema.

Only the works that belong to the `NASA ADS` application can be saved/updated into the ORCiD profile.

**WARNING**: The payload submitted to this endpoint will replace the whole ORCiD profile (ie: all 
works created by the `NASA ADS` client)


## Updating Author's works

	GET /:orcid_id/orcid-works

Returns all the works registered with ORCiD.

	POST /:orcid_id/orcid-works

Inserts one new work into the ORCiD works. The status code indicates success/failure. No payload
is returned by ORCiD.

	PUT /:orcid_id/orcid-works

Replaces all `NASA ADS` works with supplied values. This endpoint can used to remove all works.
This endpoint will return the `orcid profile` when the action was successful.

**WARNING**: Always send all the works that you want to retain.


## Logging In with ORCiD

This endpoint is used by ADS UI (Bumblebee) to obtain OAuth `access_token` (after the user
logged in with ORCiD and was redirected back to ADS). Because ORCID will always redirect to 
`https://ui.adsabs.harvard.edu/#orcid/user?code=XXXX' it is of limited use to external clients.

	GET /exchangeOAuthCode


### Parameters

Name | Type | Description
-----|------|--------------
`code`  | string | `exchange_code` issued by ORCiD

<%= headers 200 %>
```json
{"access_token":"ea12a66a-2a07-49fc-b0cb-9d0967c484c8",
 "token_type":"bearer",
 "expires_in":3599,
 "scope":"/orcid-works/create /orcid-profile/read-limited /orcid-works/update",
 "orcid":"0000-0001-8178-9506",
 "name":"Roman Chyla"
}
```

This endpoint does not need to receive `Orcid-Authorization` header.



