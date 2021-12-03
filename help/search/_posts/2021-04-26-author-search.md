---
layout: post
title: "(Advanced) Author Search"
order: 8
---

The following section describes, in ugly details, the logic of author parsing. The rules can (and will) on occassion change. But unless you have to be here and want to really know the details (or have a bit of sadomasochistic streak in yourself) just run, run away from here, quick!


## Referenced resources

[ADS solr schema](https://github.com/romanchyla/montysolr/blob/master/contrib/examples/adsabs/server/solr/collection1/conf/schema.xml#L30)



### Big Picture

OK, so what happens when we search for `author:john paul II`? 


First, the query string is turned into an abstract syntax tree (see [search parser](./2021-05-23-search-parser.md) for details) - that is the syntactic (low) level, above it there is the semantic level of parsing and modifications. 

The parser will already know we are searching inside field `author` - it will also know the tokenizer chain (rules) that apply to that field(s). So it will run the input through the tokenizer, then it will collect various outputs (tokens - more on that later), and then it will further expand/modify/transform these.

Oh, and by the way: there is a slight difference between what we do at **index** time, and the **search** time. So pay attention for it.


If you are still here, let's dive in:


### Down the Rabbit Hole

Let's take one example author: `Adamczuk, Piotr Gavrilov Eugenyi`. Heraldically attuned audience will immediately pick up that the guy is probably of Polish or Russian descent, quite likely from a noble family (blue blood runs through his veins so his name may appear next to a honorary title; but who cares? Well, our parser does). 

People are unable to remember all his names, not even editors in the scientific publications, and let's face it, they are of different origins themselves. So, some type his name as `Adamcuk`, confuse his name with `Peter`, pay no attention to uncle `Gavrilov` and can't decide whether to spell his name as `Evgenij`, `Eugenij`, `Eugen`, `Evzen` and so on. Fortunately, there aren't that many persons of female gender and name Piotr, but we can't be sure about that either (yet people will still claim it is crystal clear...)

Anyways, it is complicated - so let's start. Somebody (fortunately) for us, remembers spelling of the surname and types:


`author:peter adamczuk`


Our *search* tokenizer is going to take the input in its entirety (i.e. **NO** tokenization into `peter` and `adamzuk`) and will pass the input to a [Python library](https://pypi.org/project/nameparser/). Since the search engine is written in Java, in reality the library will be executed by Jython - so we are calling Java which looks like Python, but as you can see, I'm sparing you no details...

The library will recognize `surname` and `first name` correctly most of the time. So `Pope John Paul the II` would loose all his title and become `Paul, John` -- but we don't know anything besides the characters. We are not consulting Wikipedia to find out the real name of the Pope, nor the author (at least not yet). And our `Peter` is recognized as the first name, and `Adamczuk` as given.

Next are some boring filters: one of them normalizes the names. ` Adamczuk  ,               P ` becomes `Adamczuk, P`, and `Lao'tzu` becomes `Lao tzu,`. And we also reject any search with 6 or more names. Why? Well, because it can lead to 6^n combinations (in the worst case) in the later stages.

Next comes **transliterations** -- what's that you ask? Well, English is the Lingua Franca of scientific discourse - but only for the past two hundred years. The dominance of English alphabet in all things electronic is also a thing of the past, but humans are forever lazy (or intelligent) and when confronted with `e`, `é`, `e` .... characters, they say 'Aha! That's `e`'. All accents lost. So naturally, they want to be able to search for `jonas` and find `jonáš` as well. And so we oblige. Internally at ADS we use `UTF-8` character encoding but we don't force the English-centric writers to think in more than 26 characters of English alphabet. Also by convention, scientific publications oftentimes insist on transliterating native author names into ASCII.

So in the case of `adamczuk, p` at this stage we will discover that ADS database contains `adamčuk, peter` (we'd see also `adamčuk, p` if it was necessary)


**Intermezzo #0 - how are transliterations generated/found?**

Periodically, small minions at ADS will wake up every week, read all author names and compile a list of the following form:

```
adamczuk, p => adamčuk, p
adamczuk, peter => adamčuk, peter
adamczuk, pavel => adamčuk, pavel
```

That is, we have a set of rules - some of them custom to ADS, but the majority stemming from Java Unidecode library (the industry convention) which will transform any non-ASCII input into ASCII **transliterations**. The generated vocabulary of names has at this point millions of entries (2024917 and counting) and contains every non-Latin character that ever appeared in the ADS database. The dictionary is then used (at search time) to lookup `UTF-8` variants when users give us an `ASCII` name.

Technical note: the lookup is done via suffix trie (a search tree built by a finite state machine). So even though the dictionary has over 2M distinct entries, the cost of lookup is just the length of the input and the space occupied by the internal datastructure which is a fraction of the original size - if we were counting characters. Our 2M dictionary of names seems large, but still a far cry from the theoretical limit of 2B nodes. For details see [this nice blogpost](http://blog.mikemccandless.com/2010/12/using-finite-state-transducers-in.html) for details. 

Another option to solve this problem would be to index the transliterated names alongside with their `utf-8` originals (as ADS Classic used to do -- because it could not think in `UTF-8`) but as you will see, if you continue reading, the transliterated versions are also used to discover potential synonyms of the author's names -- so either we index all potential variants and derived synonyms, or we do all of that work at search time. There's no free lunch.

**-- end of intermezzo #0 ---**



Back to the rabbit hole: so we got the original input `peter adamzuk` -> `adamczuk, peter`, we have discovered transliteration (`adamčuk, peter`) next we proceed to discover all other names of this guy/gal. Maybe he/she got married, divorced, changed gender, remarried ... whatever the reason, the world is changing. ADS curators are being notified by authors or readers all the time and update our 'knowledge base' of author names. That is what gets consulted in this step. We'll discover that `adamčuk, peter` was previously `adamčuková, petra` (the name is made up, but such situations will exist).

Next, we'll use all of the name variants discovered so far, and take one step further -- we'll generate possible name variations, so for example authors with more than 2 names `zeta john jones` -- they could be known in the scientific literature as `zeta, j`, `zeta john, j`, and even `zeta, j j` (well, and possibly `john jones, zeta` -- if we can't tell what is the first and last name, you get the idea...)

So the parser will tentatively generate a multitude of possible names and spellings and will use them all to search for other 'real' people. If it finds anybody new, it will sigh deeply, discard the temporary variants and then proceed to generate new `transliterations` and new `synonyms` of any new (real) person that was found in ADS database. As a way of example, this is what we'll get:

- adamzuk, peter
- adamčuk, peter
- adamčuková, petra
- stoklasová, petra
- stoklasova, petra

All these names were added because our parser consulted knowledge base of author names. Our parser doesn't know this is one and the same person; but it has a way of seeing/discovering the chain of name changes. If the knowledge database is correct, which is most of the time, it will be able to start from the user input and arrive at other names. 

In the next stages, we'll deduplicate entries and normalize them once again. We'll also generate few other different queries to account for idiosynracies in how ADS stores/searches/curates data. For example, oftentimes the papers are given to ADS without full author names and will only contain initials, so even though you may want to search for the full name, we'll also (automatically) expand the search to include the initials (or vice versa - you are searching for initials but we'll insist to expand your search -- be less precise, more comprehensive). It depends on the input. If for example user typed `acamczuk, p` then our parser will assume they are fine with `adamczuk, p*` (and give them all peters, piotrs, pauls, pans and pons), but if the user typed `adamczuk, peter` then the search engine will take care not to search for `adamczuk, p*`, instead it will return `adamczuk, p`, `adamczuk, p <some other name>` and all of the synonyms thereof (`adamčuková, p`, `adamčuková, p *`, `stoklasová, p`...)

So what started as few characters (one query) is turned behind the scenes into a massive and very complicated query. There is a constant battle between the desire to be precise, and the desire to include everybody who should be there (recall). Yet all of this without really knowing much about the person, all we have is just a bunch of characters. The logic is complex, it takes advantage of what ADS knows about the authors and includes a knowledge base (plus business logic) but it is far from being able to understand 'intentions' of the user; and it has no real model of a person (and their relationships).

If it produces unexpected results, it usually is because of these reasons:

- there is a bug somewhere in this insanely complex chain -- a bug that was not caught by even the more insanely large suite of unittests (the frequency of this being the case is diminishing rapidly with time, and it happens rarely - but it is really difficult to say with certainty until the whole testsuite is examined; so it should always be the first option)
- the curated knowledge base is too broad or too narrow: i.e. it is missing a connection, or has connection too many -- and joins unrelated names together
- haphazard interferences: wrong data indexed, wrong or outdated versions of synonyms/transliterations deployed, parts of the production cluster being down, parts of the backoffice processing pipeline being down....


**Intermezzo #1**

Parts of the author search logic can be turned on/off; here are some of the most useful options:

- `=author:"adamzuk, p"` the equal sign will instruct our parser not to look for transliterations/synonyms/variants
- `author:/adamzuk,\ p/` -- you can use regular expressions, basically throwing away all the fancy logic; but mind that in the real world people really have many different names; so with this approach you will only find papers that contain just the characters of your pattern
- `author:"adamczuk, p"~0.7` -- the funny tilde float number activates a fuzzy search for the similarly sounding names. You'll need to play with the modifier until you get names that work for a particular use case (the range is 0.1-1.0). See [search parser](./2021-05-23-search-parser.md) for details.

**-- end of intermezzo #1 ---**