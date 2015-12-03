---
title: Metrics | ADS API
---

# Metrics API

{:toc}


## Requesting Metrics

	POST /metrics

### Parameters

name | type | description
-----|------|--------------
`bibcode`  |`list` | list of bibcodes
`types` | `list` | Optional. List of strings indicating type of requested report. The following values are allowed:<br/>`basic`: publication and usage stats (all papers, and just refereed papers)<br/>`citations`: citation stats<br/>`indicators`: indicators, like the h-index, g-index, m-index etc etc<br/>`histograms`: publication, citation, reads and downloads histograms<br/>`timeseries`: time series for a set of indicators
`histograms`| `list`| Optional. Only used when `types` contains value `histograms`<br/>List of histograms types, allowed values:<br/>`basic`: will return `basic stats` and `basic stats refereed`<br/>`citations`: `citation stats` and `citation stats refereed`<br/>`indicators`: `indicators` and `indicators refereed`<br/>`histograms`: `histograms`<br/>`timeseries`: `time series`




<%= headers 200 %>
``` json
{
  "basic stats": {
    "average number of downloads": 53.0, 
    "average number of reads": 77.5, 
    "median number of downloads": 53.0, 
    "median number of reads": 77.5, 
    "normalized paper count": 1.5, 
    "number of papers": 2, 
    "recent number of downloads": 3, 
    "recent number of reads": 5, 
    "total number of downloads": 106, 
    "total number of reads": 155
  }, 
  "basic stats refereed": {
    "average number of downloads": 53.0, 
    "average number of reads": 77.5, 
    "median number of downloads": 53.0, 
    "median number of reads": 77.5, 
    "normalized paper count": 1.5, 
    "number of papers": 2, 
    "recent number of downloads": 3, 
    "recent number of reads": 5, 
    "total number of downloads": 106, 
    "total number of reads": 155
  }, 
  "citation stats": {
    "average number of citations": 39.0, 
    "average number of refereed citations": 37.5, 
    "median number of citations": 39.0, 
    "median number of refereed citations": 37.5, 
    "normalized number of citations": 72.5, 
    "normalized number of refereed citations": 70.0, 
    "number of citing papers": 78, 
    "number of self-citations": 0, 
    "total number of citations": 78, 
    "total number of refereed citations": 75
  }, 
  "citation stats refereed": {
    "average number of citations": 39.0, 
    "average number of refereed citations": 37.5, 
    "median number of citations": 39.0, 
    "median number of refereed citations": 37.5, 
    "normalized number of citations": 72.5, 
    "normalized number of refereed citations": 70.0, 
    "number of citing papers": 78, 
    "number of self-citations": 0, 
    "total number of citations": 78, 
    "total number of refereed citations": 75
  }, 
  "histograms": {
    "citations": {
      "nonrefereed to nonrefereed": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "nonrefereed to nonrefereed normalized": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "nonrefereed to refereed": {
        "1998": 0, 
        "1999": 0, 
        "2000": 1, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "nonrefereed to refereed normalized": {
        "1998": 0, 
        "1999": 0, 
        "2000": 1.0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed to nonrefereed": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed to nonrefereed normalized": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed to refereed": {
        "1998": 2, 
        "1999": 3, 
        "2000": 1, 
        "2001": 1, 
        "2002": 2, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 1, 
        "2007": 1, 
        "2008": 0, 
        "2009": 1, 
        "2010": 0, 
        "2011": 0, 
        "2012": 1, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed to refereed normalized": {
        "1998": 2.0, 
        "1999": 3.0, 
        "2000": 1.0, 
        "2001": 1.0, 
        "2002": 1.5, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 1.0, 
        "2007": 0.5, 
        "2008": 0, 
        "2009": 1.0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 1.0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }
    }, 
    "downloads": {
      "all downloads": {
        "1998": 0, 
        "1999": 4, 
        "2000": 4, 
        "2001": 4, 
        "2002": 9, 
        "2003": 4, 
        "2004": 16, 
        "2005": 4, 
        "2006": 8, 
        "2007": 5, 
        "2008": 13, 
        "2009": 6, 
        "2010": 5, 
        "2011": 8, 
        "2012": 6, 
        "2013": 2, 
        "2014": 5, 
        "2015": 3
      }, 
      "all downloads normalized": {
        "1998": 0.0, 
        "1999": 3.0, 
        "2000": 4.0, 
        "2001": 3.0, 
        "2002": 9.0, 
        "2003": 4.0, 
        "2004": 14.0, 
        "2005": 4.0, 
        "2006": 7.0, 
        "2007": 4.0, 
        "2008": 12.0, 
        "2009": 5.0, 
        "2010": 3.5, 
        "2011": 7.5, 
        "2012": 5.0, 
        "2013": 2.0, 
        "2014": 4.0, 
        "2015": 1.5
      }, 
      "refereed downloads": {
        "1998": 0, 
        "1999": 4, 
        "2000": 4, 
        "2001": 4, 
        "2002": 9, 
        "2003": 4, 
        "2004": 16, 
        "2005": 4, 
        "2006": 8, 
        "2007": 5, 
        "2008": 13, 
        "2009": 6, 
        "2010": 5, 
        "2011": 8, 
        "2012": 6, 
        "2013": 2, 
        "2014": 5, 
        "2015": 3
      }, 
      "refereed downloads normalized": {
        "1998": 0.0, 
        "1999": 3.0, 
        "2000": 4.0, 
        "2001": 3.0, 
        "2002": 9.0, 
        "2003": 4.0, 
        "2004": 14.0, 
        "2005": 4.0, 
        "2006": 7.0, 
        "2007": 4.0, 
        "2008": 12.0, 
        "2009": 5.0, 
        "2010": 3.5, 
        "2011": 7.5, 
        "2012": 5.0, 
        "2013": 2.0, 
        "2014": 4.0, 
        "2015": 1.5
      }
    }, 
    "publications": {
      "all publications": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "all publications normalized": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed publications": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }, 
      "refereed publications normalized": {
        "1998": 0, 
        "1999": 0, 
        "2000": 0, 
        "2001": 0, 
        "2002": 0, 
        "2003": 0, 
        "2004": 0, 
        "2005": 0, 
        "2006": 0, 
        "2007": 0, 
        "2008": 0, 
        "2009": 0, 
        "2010": 0, 
        "2011": 0, 
        "2012": 0, 
        "2013": 0, 
        "2014": 0, 
        "2015": 0
      }
    }, 
    "reads": {
      "all reads": {
        "1998": 2, 
        "1999": 7, 
        "2000": 4, 
        "2001": 6, 
        "2002": 15, 
        "2003": 5, 
        "2004": 20, 
        "2005": 4, 
        "2006": 10, 
        "2007": 7, 
        "2008": 15, 
        "2009": 12, 
        "2010": 7, 
        "2011": 12, 
        "2012": 13, 
        "2013": 4, 
        "2014": 7, 
        "2015": 5
      }, 
      "all reads normalized": {
        "1998": 2.0, 
        "1999": 6.0, 
        "2000": 4.0, 
        "2001": 5.0, 
        "2002": 14.5, 
        "2003": 5.0, 
        "2004": 17.0, 
        "2005": 4.0, 
        "2006": 9.0, 
        "2007": 6.0, 
        "2008": 14.0, 
        "2009": 9.5, 
        "2010": 5.0, 
        "2011": 10.5, 
        "2012": 9.0, 
        "2013": 3.5, 
        "2014": 5.5, 
        "2015": 3.5
      }, 
      "refereed reads": {
        "1998": 2, 
        "1999": 7, 
        "2000": 4, 
        "2001": 6, 
        "2002": 15, 
        "2003": 5, 
        "2004": 20, 
        "2005": 4, 
        "2006": 10, 
        "2007": 7, 
        "2008": 15, 
        "2009": 12, 
        "2010": 7, 
        "2011": 12, 
        "2012": 13, 
        "2013": 4, 
        "2014": 7, 
        "2015": 5
      }, 
      "refereed reads normalized": {
        "1998": 2.0, 
        "1999": 6.0, 
        "2000": 4.0, 
        "2001": 5.0, 
        "2002": 14.5, 
        "2003": 5.0, 
        "2004": 17.0, 
        "2005": 4.0, 
        "2006": 9.0, 
        "2007": 6.0, 
        "2008": 14.0, 
        "2009": 9.5, 
        "2010": 5.0, 
        "2011": 10.5, 
        "2012": 9.0, 
        "2013": 3.5, 
        "2014": 5.5, 
        "2015": 3.5
      }
    }
  }, 
  "indicators": {
    "g": 2, 
    "h": 2, 
    "i10": 2, 
    "i100": 0, 
    "m": 0.05555555555555555, 
    "read10": 0.0, 
    "riq": 50, 
    "tori": 3.249480557003136
  }, 
  "indicators refereed": {
    "g": 2, 
    "h": 2, 
    "i10": 2, 
    "i100": 0, 
    "m": 0.05555555555555555, 
    "read10": 0.0, 
    "riq": 50, 
    "tori": 3.249480557003136
  }, 
  "skipped bibcodes": [], 
  "time series": {
    "g": {
      "1998": 1, 
      "1999": 1, 
      "2000": 1, 
      "2001": 1, 
      "2002": 1, 
      "2003": 1, 
      "2004": 1, 
      "2005": 1, 
      "2006": 1, 
      "2007": 1, 
      "2008": 1, 
      "2009": 1, 
      "2010": 1, 
      "2011": 1, 
      "2012": 1, 
      "2013": 1, 
      "2014": 1, 
      "2015": 1
    }, 
    "h": {
      "1998": 1, 
      "1999": 1, 
      "2000": 1, 
      "2001": 1, 
      "2002": 1, 
      "2003": 1, 
      "2004": 1, 
      "2005": 1, 
      "2006": 1, 
      "2007": 1, 
      "2008": 1, 
      "2009": 1, 
      "2010": 1, 
      "2011": 1, 
      "2012": 1, 
      "2013": 1, 
      "2014": 1, 
      "2015": 1
    }, 
    "i10": {
      "1998": 1, 
      "1999": 1, 
      "2000": 1, 
      "2001": 1, 
      "2002": 2, 
      "2003": 2, 
      "2004": 2, 
      "2005": 2, 
      "2006": 2, 
      "2007": 2, 
      "2008": 2, 
      "2009": 2, 
      "2010": 2, 
      "2011": 2, 
      "2012": 2, 
      "2013": 2, 
      "2014": 2, 
      "2015": 2
    }, 
    "i100": {
      "1998": 0, 
      "1999": 0, 
      "2000": 0, 
      "2001": 0, 
      "2002": 0, 
      "2003": 0, 
      "2004": 0, 
      "2005": 0, 
      "2006": 0, 
      "2007": 0, 
      "2008": 0, 
      "2009": 0, 
      "2010": 0, 
      "2011": 0, 
      "2012": 0, 
      "2013": 0, 
      "2014": 0, 
      "2015": 0
    }, 
    "read10": {
      "1998": 0, 
      "1999": 0, 
      "2000": 0, 
      "2001": 0, 
      "2002": 0, 
      "2003": 0, 
      "2004": 0, 
      "2005": 0, 
      "2006": 0, 
      "2007": 0, 
      "2008": 0, 
      "2009": 0, 
      "2010": 0, 
      "2011": 0, 
      "2012": 0, 
      "2013": 0, 
      "2014": 0, 
      "2015": 0.0
    }, 
    "tori": {
      "1998": 2.9862644544853527, 
      "1999": 3.0169389412386467, 
      "2000": 3.1892078488016717, 
      "2001": 3.1966705353688365, 
      "2002": 3.2207562856840948, 
      "2003": 3.2207562856840948, 
      "2004": 3.2207562856840948, 
      "2005": 3.2207562856840948, 
      "2006": 3.227899142826952, 
      "2007": 3.239010253938063, 
      "2008": 3.239010253938063, 
      "2009": 3.2478598114601867, 
      "2010": 3.2478598114601867, 
      "2011": 3.2478598114601867, 
      "2012": 3.249480557003136, 
      "2013": 3.249480557003136, 
      "2014": 3.249480557003136, 
      "2015": 3.249480557003136
    }
  }
}

```


## Explanation of Field Values

Each of these attributes contains specific data elements. The following overview shows what each section contains (the phrases listed are the attribute names).

### `basic stats` and `basic stats refereed`
  * number of papers
  * normalized paper count
  * median number of reads
  * average number of reads
  * total number of reads
  * normalized number of reads
  * median number of downloads
  * average number of downloads
  * total number of downloads
  * normalized number of downloads

### `citation stats` and `citation stats refereed`
  * number of citing papers
  * median number of citations
  * average number of citations
  * total number of citations
  * normalized number of citations
  * median number of refereed citations
  * average number of refereed citations
  * total number of refereed citations
  * normalized number of refereed citations
  * number of self-citations

### `indicators`
  * i10
  * i100
  * h
  * m
  * g
  * read10
  * tori

### `histograms`

For all histograms, the actual histogram values are stored as follows:

```json
  {
   "histogram name": {year: value, year: value, ...}
  }
```

Where values can be either integers or floats, depending on the type of histograms. The histogram name is an attribute of the histogram type. For example, the `publications` type has 4 separate histograms: `all publications`, `refereed publications`, `all publications normalized` and `refereed publications normalized`, which are organized as follows in the JSON output:

```json
    {
	    "histograms":  {
			"publications": {
				"all publications": {},
				"refereed publications": {},
				"all publications normalized": {},
				"refereed publications normalized": {}
			}
		}
	}
```

The following overview lists for all histogram types the names of the actual histograms stored in them:

  * `publications`: `all publications`, `refereed publications`, `all publications normalized`, `refereed publications normalized`
  * `reads`: `all reads`, `refereed reads`, `all reads normalized`, `refereed reads normalized`
  * `downloads`: `all downloads`, `refereed downloads`, `all downloads normalized`, `refereed downloads normalized`
  * `citations`: `refereed to refereed`, `nonrefereed to refereed`, `refereed to nonrefereed`, `nonrefereed to nonrefereed`, `refereed to refereed normalized`, `nonrefereed to refereed normalized`, `refereed to nonrefereed normalized`, `nonrefereed to nonrefereed normalized`

Note that `refereed reads` means: 'number of reads for the refereed publications in the set'.



### Examples 

Curl, requesting the `basic` metrics::

``` command-line
$ curl -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -X POST -d '{"bibcodes":["1980ApJS...44..137K","1980ApJS...44..489B"], "types": ["basic"]}' https://api.adsabs.harvard.edu/v1/metrics
> {
>   "basic stats": {
>     "average number of downloads": 53.0, 
>     "average number of reads": 77.5, 
>     "median number of downloads": 53.0, 
>     "median number of reads": 77.5, 
>     "normalized paper count": 1.5, 
>     "number of papers": 2, 
>     "recent number of downloads": 3, 
>     "recent number of reads": 5, 
>     "total number of downloads": 106, 
>     "total number of reads": 155
>   }, 
>   "basic stats refereed": {
>     "average number of downloads": 53.0, 
>     "average number of reads": 77.5, 
>     "median number of downloads": 53.0, 
>     "median number of reads": 77.5, 
>     "normalized paper count": 1.5, 
>     "number of papers": 2, 
>     "recent number of downloads": 3, 
>     "recent number of reads": 5, 
>     "total number of downloads": 106, 
>     "total number of reads": 155
>   }, 
>   "skipped bibcodes": []
> }

```

Python:

```python
payload = {'bibcodes': ['bibcode1', 'bibcode2']}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization':'Bearer %s' % token}
r = requests.post(queryURL, data=json.dumps(payload), headers=headers)
```
where `token` is your API token.

## Source Code

The source of the microservice is at https://github.com/adsabs/metrics_service.


