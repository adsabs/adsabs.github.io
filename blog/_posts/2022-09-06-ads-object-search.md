---
layout: blog_post
title: "The ADS Object Search - How to Find Astronomical Objects in the Literature"
author: "Edwin Henneken"
position: "ADS"
category: blog
label: general
thumbnail: blog/images/blog_2022-09-06_objectsearch.png
---
Searching for publications that mention, in some way, a specific astronomical object is one of the common use cases of the ADS. This blog aims to illustrate some of the caveats associated with these types of queries and provide some pointers.

If a publication mentions an astronomical object in its title or abstract, this object probably plays a significant role in this publication. If the object only appears in the body of the paper, the object most likely appears as part of a catalog or in a less prominent role. If your goal is, for example,  to find publications that focus on the star Aldebaran, you search for mentions in basic metadata (title, keywords or abstract). This is precisely the function of the so-called "unfielded query" in the ADS. Unfielded queries, without query fields[^1], will search the basic metadata of the publications (author, publication year, title, abstract, keywords). In the case of our example, focusing on publications in the astronomy collection, this query is

```
Aldebaran collection:astronomy
```

[^1]:A query field in general has the format of a field name, directly followed by a colon (like e.g. `author:`). The result of a fielded query is that only specific data types in our database are queried with the data provided (see [this page](https://ui.adsabs.harvard.edu/help/search/comprehensive-solr-term-list) in our online Help for a comprehensive list of query fields)

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads-object-search_f1.png" />
<em>Figure 1</em>
</div>
<br>

Before going into specifics of search technicalities, let's first explore the question of the necessity of adding the collection filter (restricting the query to the ADS Astronomy collection). The ADS holdings cover a wide range of disciplines; this is the result of indexing multidisciplinary publications like Science, Nature and arXiv e-prints, but also because we include the literature that is cited by and which cites the core literature. This is an important fact to keep in mind when exploring the ADS holdings. Often, names of astronomical and planetary objects are taken from areas like mythology. It also happens that, for example, projects, services or companies, unrelated to astronomy, are named after astronomical objects (like Aldebaran Robotics). Records not fetched by the query above are retrieved by the query ```Aldebaran NOT collection:astronomy```. Inspection of the results show publications that are definitely related to the star Aldebaran. As illustrated in the screenshot (Figure 1), it helps to check the highlights for the context of the matches. For example, the arXiv record [The Ancient Astronomy of Easter Island: Aldebaran and the Pleiades](https://ui.adsabs.harvard.edu/abs/2016arXiv161008966R/abstract) (in the arXiv category `Physics - History and Philosophy of Physics`) and the SPIE record [Measurement of the speed of light from extraterrestrial sources](https://ui.adsabs.harvard.edu/abs/2015SPIE.9608E..0EW/abstract). There are also records that are obviously unrelated to the star (e.g. humanoid robots, Aldebaran Sandstone). In the ADS curation workflow we attempt to classify records from multidisciplinary sources (like the journals Science and Nature). In some cases it may be better to optimize your query beforehand (by adding filters), while in other cases it will be better to cast a wide net first and apply filters afterwards. The best strategy depends on one's goals.

From a technical point of view, whether the aforementioned query finds more than just records that literally mention `Aldebaran` in their basic metadata, depends on if the search engine has been made aware of the fact that the star Aldebaran is also known in other ways. These are the so-called synonyms. Whether the ADS has synonyms listed for Aldebaran (or any term, for that matter) can be checked by running a query for the term and excluding any literal mentions of that term (by switching off synonym replacement, using the = modifier)

```
Aldebaran NOT =Aldebaran collection:astronomy
```

In our [example](https://ui.adsabs.harvard.edu/search/q=Aldebaran%20NOT%20%3DAldebaran%20collection%3Aastronomy&sort=date%20desc%2C%20bibcode%20desc&p_=0), this just returns 1 record. The `Show Highlights` feature in the search results page shows that the ADS has the synonym Aldeberan included in its index. This means that the ADS is NOT aware of synonyms like: Alpha Tauri, alf Tau, alpha Tau, HD 29139, GC 5605. How does this impact search results? For example, the following query returns about 200 more records:

```
(Aldebaran OR "Alpha Tauri" OR "alf Tau") collection:astronomy
```

The synonyms in the ADS are the result of manual curation. The ADS team maintains correspondences between terms and their synonyms; besides concepts, synonyms also exist for author names and acronyms. The existence of synonyms means that queries involving such terms are expanded to include all of the synonyms supplied. The search engine is also able to interpret Unicode characters: the query `α Tau` is supported. Even though there are publications that refer to Aldebaran just by `α Tau`, this query is probably not an ideal general query strategy, because of all the false positives (like matches on `α/√(τ+1)`, `α /τ`, `Omega = alpha/tau`) and even the phrase `scale index α, where τ` (because `where` is a stop word). 

Obviously, the ADS cannot maintain a correspondence of all synonyms for all known astronomical and planetary objects. Fortunately, the ADS does not need to: for decades the ADS has collaborated with the NASA/IPAC Extragalactic Database (NED) and SIMBAD of the Centre de Données astronomiques de Strasbourg (CDS). The collaboration with SIMBAD started in 1993, and was the first real time joint scientific database query spanning continents. The CDS has developed DJIN (Detection in Journal of Identifiers and Names) ([Lesteven et al. (2010)](https://ui.adsabs.harvard.edu/abs/2010ASPC..433..317L/abstract)). This system suggests a list of astronomical objects (indexed in the SIMBAD database), automatically recognized in each article. In this way, since 2008, the references are linked to the SIMBAD astronomical objects rapidly after publication. The new objects and those that are not yet in SIMBAD are added manually in the database with the respective ADS bibliographic identifiers (bibcodes) and data. The CDS documentalist team uses its expertise to validate the possible matches proposed by DJIN and corrects all errors or omissions by the software. The CDS shares these correspondences with the ADS. Using this index, the ADS maintains an index of bibcodes, object types and their canonical names. Something similar happens for NED. How can these correspondences be accessed? There is nothing about the unfielded query

```
Aldebaran collection:astronomy
```

that will cause the ADS search engine to make use of these correspondences provided by SIMBAD and NED. This is the function of the `object:` query field. Whatever is supplied to this query field will be interpreted by the search engine as a Boolean expression of astronomical object names (example: `object:((SMC OR LMC) AND M31)`). Alternatively, one can use the `Object` box in the ADS [Classic Form](https://ui.adsabs.harvard.edu/classic-form) (see Figure 2). Information specified in this form will get translated into an ADS search with query fields.

What happens when the `object:` query field is used? Since we cannot assume that a user will specify canonical object names in their queries, we need to make sure that the object names provided are translated into their canonical equivalents. This is because SIMBAD and NED provide us correspondences between publications and canonical names of objects. Both SIMBAD and NED provide a translation service. Having established these canonical equivalents, the ADS search engine is able to find all associated publications, according to the Boolean relationship specified. Additionally, the object names (as specified in the query) are also used in an ADS query against abstracts, titles and keywords in the astronomy collection (with synonym replacement switched off). The result set is a combination of all these matches. Object queries that target just one service (e.g. SIMBAD) are not currently supported.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/ads-object-search_f2.png" />
<em>Figure 2</em>
</div>
<br>

What difference does the `object:` query field make for our example query? The query

```
object:Aldebaran collection:astronomy
```

returns ~1,440 results (instead of the ~260 without the query field). The filter on collection is strictly not necessary because the `object:` search will, per definition, return records with SIMNAD/NED links (which all are in the Astronomy collection).

Caveat: the `object:` search will not return publications not covered by SIMBAD and/or NED and if the object appears with a different name than the one specified in the query. This may be a temporary situation (it takes time for the SIMBAD and NED teams to process publications), unless a publication mentioning the object is not covered by SIMBAD or NED. For example, if an arXiv record mentions Aldebaran using its synonym `HD 29139`, the query above will not find this record.

As expected, extending the search to include full text will significantly increase the number of matches. The ADS supports two query fields to include full text: `full:` and `body:`. The difference is that `full:Aldebaran` searches for publications with `Aldebaran` in a number of fields (title, abstract, body, acknowledgements and keywords) and `body:Aldebaran` searches for papers containing `Aldebaran` in just the body of an article. The obvious caveat here is that these queries only cover those records in the ADS for which full text has been indexed. In general, [this query](https://ui.adsabs.harvard.edu/search/q=fulltext_mtime%3A%5B%221000-01-01t00%3A00%3A00.000Z%22%20TO%20*%5D&sort=date%20desc%2C%20bibcode%20desc&p_=0) returns all records with full text; all major astronomy journals are among these records.

The table below displays the number of records found through different search strategies (as found on Aug 29, 2022)

Query | Number of records found
Aldebaran collection:astronomy | 263
(Aldebaran OR "Alpha Tauri" OR "alf Tau") collection:astronomy | 456
"α Tau" collection:astronomy | 224
object:Aldebaran collection:astronomy | 1,443
body:Aldebaran collection:astronomy | 4,759

Finally, a few words on the topic of the range of objects covered by the `object:` search. At first, (in 1971 as the Catalog of Stellar Identifications), SIMBAD focused only on stars in the Milky Way, but since about 1982 it has been extended to all objects outside the Solar System. NED focuses on extragalactic objects. How about objects inside the Solar System, like Minor Planets? A quick search in the [Sesame](https://cds.u-strasbg.fr/cgi-bin/Sesame) service for e.g Haumea shows that there are no entries in either SIMBAD or NED (as expected), so the query `object:Haumea` will only search the basic metadata in the ADS. The query still finds 234 records, most of which seem relevant. However, this list probably is not exhaustive and is probably missing some key publications. Before this dwarf planet was known as `Haumea`, it had the MPC designation `2003 EL61`. We can get an indication of literature about this dwarf planet in this early stage by means of the query

```
 ="2003 EL61" NOT Haumea
```

This returns 81 records, like [2005ApJ...632L..45B](https://ui.adsabs.harvard.edu/abs/2005ApJ...632L..45B/abstract), the first refereed publication mentioning this dwarf planet. Searching for Haumea would not have found this publication. This situation can be improved by making use of a service like [Quaero](https://ssp.imcce.fr/webservices/ssodnet/api/quaero/). A query of the [Quaero API](https://api.ssodnet.imcce.fr/quaero/1/sso/Haumea) (hosted at IMCCE , Paris Observatory) for `Haumea` returns

```
{"name":"Haumea","physical-ephemeris":true,"type":"Dwarf Planet","class":["KBO","SDO"],"system":"Haumea","aliases":["136108","2003 EL61","2136108","D6108","K03E61L"],"physical-models":[1],"id":"Haumea","updated":"2022-08-22","parent":"Sun","ephemeris":true}
```

The good news is that ​​we will improve the usefulness of ADS for scientists involved in Planetary Sciences and Heliophysics research, by enhancing our system so that it becomes aware of the specific terminology used by practitioners in the disciplines. Over the next year or two, we'll be augmenting the object search in these disciplines by adding the Quaero API and similar services to our object field search.