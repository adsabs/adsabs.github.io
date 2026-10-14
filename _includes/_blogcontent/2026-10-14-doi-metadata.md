<h3 style="margin-top: 0; color: #5FBFAE;">Introduction</h3>

<figure style="float: left; width: 350px; margin: 1em 1.5em 1em 0; text-align: center;">
  <img src="{{site.baseurl}}/blog/images/blog_2026-10-14-metadata-cartoon.png" 
      alt="Two-panel cartoon: a sweating man hesitates between two red buttons labeled 'Create metadata' and 'Let user guess what's in dataset.'"
      class="img-responsive" 
      style="width: 100%;">
  <figcaption style="font-size: 0.85em; color: #8da09a; margin-top: 0.5em;">
    "With great metadata comes great responsibility."
  </figcaption>
</figure>

Metadata is the lifeblood of publishing in the digital age and the key to discovery and attribution. Metadata permeates and enables all aspects of publishing. It is essential for publishers, authors, and all others involved in the publishing industry to understand the metadata ecosystem in order to maximize the resources that contribute to a title’s presence, popularity, and reuse. In other words, there are many stakeholders involved in this world of metadata. Metadata and the associated processes to use it are evolving, becoming more interconnected and social, enabling linkages between a broad network of digital objects and resources. So, bad metadata will travel through this interconnected web and will cause all kinds of headaches for everybody involved; bad metadata can refer to badly formatted metadata, ambiguous metadata, incomplete metadata and all kinds of other reasons causing it to not accurately represent the object it is supposed to describe (the importance of accurate metadata for data products in the astronomy community is e.g. discussed in [Blanton et al. 2023](https://scixplorer.org/abs/2023arXiv231104272B/abstract)). 

In the case of metadata associated with DOIs, it starts with the process of registering the DOIs. A decision is made that a particular digital object needs to have a DOI. Depending on the characteristics of this object, it will get registered with either Crossref or DataCite[^1]. Hopefully, the persons in charge of registering the DOI will consult the metadata model of the target registry and make decisions on what information goes where during the registration process. Practice has shown that many things can (and do) go wrong here. Generating descriptive metadata requires thorough understanding of the digital object and how to translate this into the metadata model of the registrar; insufficient knowledge of, or ambiguities in the metadata model will translate into an inaccurate representation of a digital object in terms of DOI metadata. Putting a string like "Smith, J. et al. (2020)" in the place where the author name is supposed to be is an example of incorrect metadata. Specifying just a file name as title is an example of lacking descriptive metadata. 

As mentioned earlier, metadata is key to discovery. A service like the Science Explorer (SciX) supports the discovery of products generated during a research life cycle. So, the efficacy of a service like the SciX hinges on accurate metadata. For some of its holdings, SciX depends on metadata associated with DOIs, whether from Crossref or DataCite (or any other registrar). So, if bad metadata is registered with a DOI, bad metadata enters the SciX indexing process and bad information is disseminated to the users of our service. Those users, when writing their paper, export records from SciX to include in their bibliographies. This way inaccuracies get injected into the scholarly publishing workflow. Some journal editors may catch and correct these errors, but it is likely that many of those inaccuracies will not get caught.

The following section describes how DOIs get used in the process of ingesting and indexing publications.

<h3 style="margin-top: 0; color: #5FBFAE;">Use of DOI metadata in SciX</h3>

SciX relies heavily on DOI metadata from both Crossref and DataCite. It is no exaggeration to say that the functionality of SciX hinges on Crossref DOI metadata; for journals for which we do not have a direct feed from the publisher, Crossref is the only source of article and reference metadata. Getting metadata for DataCite DOIs was introduced with the [Asclepias project](https://scixplorer.org/scixblog/asclepias).

While in the past, our focus was to generate metadata files in the [ADS tagged format](https://ui.adsabs.harvard.edu/help/data_faq/tagged-format), it is now better to refer to the SciX [Ingest Model](https://github.com/adsabs/ingest_data_model). When ingesting metadata associated with DOIs, we need to verify whether this metadata is compatible with our data model. The need for this verification is particularly relevant with our expansion into new disciplines, where other, additional types of information are relevant, but also with the increased ingest of non-traditional digital objects like data products. The section on using metadata from DataCite DOIs will highlight this.

<h3 style="margin-top: 0; color: #5FBFAE;">Use of metadata from Crossref DOIs</h3>

Traditionally, the requirement for Crossref metadata was that it provides a sufficient amount of information to create a record: an author list (preferably complete), a title, and journal information (name, publication year, volume, page identifier). An abstract is not a requirement, nor is affiliation information. If references are included in the Crossref record, they will be taken as well. Our [parsing](https://github.com/adsabs/ADSIngestParser/blob/main/adsingestp/parsers/crossref.py) of Crossref metadata has moved well beyond the retrieval of the minimal set of required metadata and includes information like author ORCiDs. We keep extending this workflow to include more information as we learn more about relevant pieces of metadata for other disciplines, like Earth Science.

<h3 style="margin-top: 0; color: #5FBFAE;">Use of DataCite DOIs</h3>

Our systematic use of DataCite DOIs started with the Asclepias project. The [Citation Capture Pipeline](https://github.com/adsabs/ADSCitationCapture), specifically developed for this project, currently looks for references that cite works with a Zenodo DOI. When such a DOI is detected, the associated metadata is harvested from DataCite, and if this turns out to be a software DOI, appropriate action is taken. A new record is created based on the DataCite metadata if no SciX record exists yet. In addition this software citation capture will trigger a `Cites` event to Zenodo's broker, creating a relationship between the canonical version of the citing bibcode (we use the API to obtain the canonical if it exists) and the DOI. It will also trigger an `IsIdenticalTo` event to Zenodo's broker, creating a relationship between the DOI and the newly created bibcode of the record that will be indexed.

We have started to systematically harvest DataCite metadata for the following sources:

- Publications
    - Zenodo: specific user-defined collections 
    - MPEC: Minor Planet Circular
    - LSST: NSF-DOE Vera C. Rubin Observatory Technical Reports
- Data Sets
    - PDS: NASA Planetary Data System Data
    - JAXA: JAXA Data
    - IPAC: NASA IPAC Data
    - NASA DAAC: NASA Distributed Active Archive Center Data
    - NASA OSDR: NASA Open Science Data Repository
    - NASA PSI: NASA Physical Sciences Informatics
    - USGS: United States Geological Survey
    - IEDA: Interdisciplinary Earth Data Alliance

The main goal of the DataCite harvests is obtaining sufficient metadata to create records and, if appropriate, assign citations. Extending the indexing of data products beyond PDS data, is relatively recent. This extension has already shown us how challenging indexing dataset metadata can be, for all of the reasons mentioned above (see our [blog on indexing data products](https://scixplorer.org/scixblog/data-linking-III)). Unlike the registration of Crossref DOIs for journal articles, there is, in general, no quality control for the registration of dataset DOIs. The query [`doctype:dataset`](https://scixplorer.org/search?p=1&q=doctype%3Adataset&sort=score+desc&sort=date+desc&d=astrophysics) returns all data products currently indexed in SciX. Inspection of the author facet illustrates one particular aspect of the challenge. The population of this facet is based on author information in the SciX ingest data model; for metadata harvested from DataCite, author information is based on the `creator` element. [Description](https://datacite-metadata-schema.readthedocs.io/en/4.5/properties/creator/) of this element in the DataCite metadata schema indicates that this can represent a corporate/institutional or personal name. Inspection of the SciX author facet shows that there are entries that are neither, unless the concept of the corporate/institutional name is interpreted very loosely. The DataCite metadata schema supports the specification of the type of contributor through the `nameType` attribute; this attribute supports two values from a controlled vocabulary: `Organizational` or `Personal`. An entry like the following one is unfortunate for two reasons: first, the name is not really an institutional name and second, the name type was not specified:

```xml
  <creators>
    <creator>
      <creatorName>Precipitation Processing System (PPS) at NASA GSFC</creatorName>
    </creator>
  </creators>
```

In SciX, this example resulted in an "author" entry `NASA GSFC, P.` in the author facet.

The SciX discovery mechanism is not ideal either. Institutional "authors" are being forced into the "last name, first name(s)" model. A query like `author:"NASA Ocean Biology Processing Group"` returns correct results, except one record that has an author `Group, N. W.` The query `author:"NASA Ocean Biology Processing Group,"` would have prevented this (by appending the comma at the end). The best we can do, for cases like these, is to provide better representation of institutional authors in queries and detect the name type in those cases when `nameType` is not specified in the metadata.

We are still actively discussing the act of indexing datasets; this is not necessarily a discussion on whether to index them, but mostly on how and which datasets. We will definitely need to update our internal metadata schema, because datasets are far more complex digital objects than publications. Examples of topics we need to have internal discussions about:

- Creator/contributor roles (see e.g. the [Contributor Role Taxonomy](https://credit.niso.org/))
- Active datasets
- Collections
- What other metadata fields to capture

---

[^1]: There are other DOI registries: [https://www.doi.org/the-community/existing-registration-agencies/](https://www.doi.org/the-community/existing-registration-agencies/). Some of these registries might have an underlying metadata model and API, others like China's do not.

