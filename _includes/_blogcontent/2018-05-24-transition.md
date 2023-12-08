
### Update (April 12, 2019)
Classic's retirement timeline has been adjusted slightly. We plan to begin disabling searching in Classic in May 2019, with full site retirement slated for Q3 2019. For more on steps to take before that time, see [our post on things to do before the transition](../blog/transition-reminder).

### Original post
ADS is excited to announce that the [new ADS interface](https://ui.adsabs.harvard.edu/), codenamed Bumblebee, is leaving its beta label behind! The service, under development since 2015, has reached parity with ADS Classic. In addition, it provides a modern interface and new search features.

ADS Classic, in service since 1994, will be phased out over the next year and will be retired on May 31, 2019. While it has served its original purpose well, still serving roughly 50,000 unique users a day and around three-quarters of a million unique users a month, Classic’s 90s-era infrastructure makes it impossible to continue to scale and to incorporate more modern search features. (For the curious, check out our [more technical post](../blog/technical) about what’s under the hood of both Classic and Bumblebee.)

The new ADS offers a convenient one-box search, much like web search engines. It accepts both fielded and unfielded queries. For fielded queries, the required search field (such as author:) is entered along with the search terms in order to narrow the scope of the search. Unfielded queries are entered without field tags and search in all metadata fields: author; publication year; title; abstract; identifier, such as bibcodes and DOIs; and bibstem, or the shortened form of publication names (e.g. ApJ, SPIE, AAS). The new ADS also offers a [Classic Search form](https://ui.adsabs.harvard.edu/#classic-form), which reproduces the multi-box search form in Classic, for those unfamiliar with one-box searching. New users are also encouraged to check out our [documentation](../help/), especially our [Quick Start](../help/quickstart) and [Search Syntax](../help/search/search-syntax) guides.

Behind the scenes, the new ADS utilizes the Apache Solr search engine, which can index a much larger amount of data than Classic and enables more flexible searching (see the [technical blog post](../blog/technical) for more details). Some examples of new types of searches now available:
- Filtering search results is enabled through the use of the left-side menu filter facets, allowing users to quickly narrow down a large list of search results without editing the original query
- Full text searches are now available for over 4 million of our 13 million records, including most recent articles
- New fields, such as author affiliations and acknowledgements sections, are now indexed and searchable where available
- [Positional searches](../help/search/positional), such as searches for a known second author, are now possible
- [Second order queries](../help/search/second-order) are available, enabling sophisticated topic-based searches, such as for trending papers

The new interface also allows for filtering and manipulation of the entire results set, while in Classic users were limited to working with a maximum of 3000 records.

Other improvements have been made, such as integration with [ORCID](https://orcid.org/), allowing users to [claim](../help/orcid/claiming-papers) their own papers or to [search](../help/orcid/orcid-search) using a known ORCID ID. This allows for easier assembly and sharing of personal bibliographies. In addition, graphics and figures are available for articles when provided by the publisher. This provides a quick preview of the data discussed in the paper and its main results. The new ADS also offers new ways to [visualize](../help/actions/visualize) data, including author networks and related papers.

Development on the new interface is ongoing, with new features and improvements continually rolled out. Some things we’re working on now include improved author affiliation searching and filtering, better ORCID integration, improved recommendations, and better support for software citations. Keep an eye on our [blog](../blog/) or [social](https://twitter.com/adsabs) [media](https://www.facebook.com/nasaads) for the latest!

We hope you enjoy the new search interface. However, if you get stuck or encounter an issue, [drop us a line](mailto:adshelp@cfa.harvard.edu).
