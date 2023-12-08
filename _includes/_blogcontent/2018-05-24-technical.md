
In this post, we’d like to give you a peek under the hood of both ADS Classic and the new ADS service.

**ADS Classic**

ADS Classic went online on the nascent World Wide Web in 1994. In the early 1990s, databases such as SQL were fairly slow and had other limitations, including strict restrictions on the number of characters allowed in individual fields. These limitations made the databases of the day inadequate for ADS’s original purpose of indexing the abstracts of the published astronomy literature.

So the ADS created its own custom ingestion, indexing, and search system using C and Perl. All software was created from scratch and was structured as a single monolithic piece of software. This custom system does not use a conventional database engine but instead indexes flat files on disk. Each record is identified by a 19-character [bibcode](../../help/actions/bibcode) and points to multiple files: bibliographic data are stored in formatted text files and non-bibliographic data, such as data links and usage statistics, are stored in separate column files. References are stored in separate files and regularly reprocessed to match citations with existing ADS records.

When new records are ingested or updates are made to existing records, the bibliographic text files are processed and new indices are created and written to disk. These index files are loaded into the server’s shared memory; all searches are in-memory binary searches.

As the ADS has grown and started to index new fields and new types of data, the limits this custom system imposes on the way data can be structured have become obvious. Work started on the new generation of the ADS, including previous iterations, such as ADS 2.0, and the current new ADS interface, in 2009.

**The New ADS**

In contrast to the monolithic architecture of ADS Classic, the new ADS, codenamed Bumblebee, is built on a framework of individual microservices communicating via application programming interfaces, or APIs. Each component of Bumblebee, such as libraries or metrics, lives in its own independent microservice. This modularity allows functionality to be added to individual components or for each component to scaled up as needed to support user traffic without affecting the rest. [Kubernetes](https://kubernetes.io/) is used to manage the microservice loads and to scale their availability in real time to match current usage. 

In fact, the connection between the back-end search engine and the [front-end search interface](https://ui.adsabs.harvard.edu/) is also mediated by an API. The web-based interface and the search engine exist as separate components, unlike in Classic. The same search engine API that the web-based interface uses can be accessed by regular users via command line scripts. More information can be found on our [help pages](../../help/api/) and our Github-based [instruction manual](https://github.com/adsabs/adsabs-dev-api).

The new ADS uses a modern, open-source, enterprise-level search engine, Apache Solr, which is built on the Apache Lucene library and is used by both academic institutions and commercial companies. Out of the box, Solr enables a variety of advanced search options, included fielded and unfielded queries, approximate searches, and wildcard searches. Its high-performance, scalable architecture allows us to index not just the basic article information (metadata) but also the full-text contents of each article, a highly requested feature from the library community.  Our implementation of Solr has been heavily modified for our use, including the addition of [second-order operators](../../help/search/second-order) such as trending() and familiar ADS Classic operators like the first-author search caret (^).

The new ADS is also now open-source: the microservices, back-end data pipelines, and front-end codebase are available on [Github](https://github.com/adsabs). The service is no longer hosted on local servers or on [mirror servers](http://adsabs.harvard.edu/mirrors.html), but is instead cloud-based and hosted by Amazon Web Services. This should improve the speed and reliability of the new ADS over Classic.

Overall, these improvements to the structure and hosting of ADS bring searching the astronomy literature into the 21st century. The new ADS has reached feature parity with Classic and work is ongoing to continue to improve it and add new functionality. If you have any feedback or suggestions, let us know using the Feedback form available in Bumblebee.
