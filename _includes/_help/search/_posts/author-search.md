The following section describes, in ugly detail, the logic of author parsing and searching. 


## Referenced resources

[{{ include.site }} solr schema](https://github.com/adsabs/montysolr/blob/main/deploy/adsabs/server/solr/collection1/conf/schema.xml#L30)



## Big Picture

What happens when we search for `author:"Adamczuk, Peter"`? 

First, the query string is turned into an abstract syntax tree (see [search parser](./search-parser) for details). The query parser will see that we are searching the field `author` and apply the tokenizer chain (rules) specified for that field. So it will run the input through the author tokenizer, which has a number of steps involved in transforming the input text into what gets indexed and searched. 

There is also quite a difference between what we do at **index** time, and at the **search** time in order to optimize searches and maximize both precision and recall.

### Details

Let's consider as an example the case of an author whose full name is `Adamčuk, Piotr Gavrilov Eugenyi`.

People using our search engine may be unable to remember all his names, misremember the last name as `Adamczuk`, assume his first name with `Peter` (which he has occasionally published under), and not know about his additional middle names `Gavrilov` and `Eugenyi` which might have been transcribed in the past in multiple ways such as `Evgenij`, `Eugenij`, `Eugen`, `Evzen`.

As you can imagine, balancing accuracy and retrieval for author names searches is going to be tricky. Let's imagine that a user searches for this scientist's paper using the following query:

```
author:"peter adamczuk"
```

#### Normalization

The first step we perform is name normalization, in order to ensure that the author name is properly formatted. Our *search* tokenizer is going to take the input in its entirety (the full string `peter adamczuk` with **NO** tokenization into `peter` and `adamczuk`) and will pass the input to a [name parsing Python library](https://pypi.org/project/nameparser/). Since the search engine is written in Java, in reality the library will be executed by [Jython](https://www.jython.org/).

The library will parse the input string to identify its components: surname, first name, and optionally middle name(s), titles, suffixes, etc. So `Pope John Paul the II` would lose all his titles and be normalized to `Paul, John, II`. In our example, `Peter` is recognized as the first name, and `Adamczuk` as the last name.

Normalization also involves removal of excessive whitespace, punctuation, hyphens, apostrophes, etc. For example, `Adamczuk  ,               P ` becomes `Adamczuk, P`, and `Lao'tzu` becomes `Lao tzu,`. We also limit the number of names allowed for a single author to 6 tokens.

#### Transliteration

The next step involves name transliterations, which map "similar" classes of characters to a common format. English is the Lingua Franca of scientific discourse, but author names span a huge variety of character sets. Transliterations allow author names containing a variety of accented characters to be found when searching for their ASCII equivalent. For example, a search for `jonas` would find the name `jonáš` as well. Internally in our database we use the `UTF-8` character encoding so that we can properly represent the original author name but we don't force the English-centric writers to think in more than 26 characters of the English alphabet. 

So in the case of `adamczuk, p` at this stage we will discover that the {{ include.site }} database contains `adamčuk, peter` and any of its variations such as `adamčuk, p` if present.


How are transliterations generated and managed? We periodically go through our author index and for each name not already in ASCII format we generate its equivalent mappings, for example:

```
adamczuk, p => adamčuk, p
adamczuk, peter => adamčuk, peter
adamczuk, piotr => adamčuk, piotr
```

Some of the transliteration rules are custom to {{ include.site }}, but the majority stemming from Java Unidecode library. The generated vocabulary of names has at this point millions of entries and contains every non-Latin character that has ever appeared in the {{ include.site }} author database. The dictionary is then used (at search time) to lookup `UTF-8` variants when users give us an `ASCII` name.

#### Synonyms

Normalization and transliteration transform the original input from `peter adamzuk` to `adamczuk, peter`, to (`adamczuk, peter`, `adamčuk, peter`). Next we proceed to discover all other known names of this person. {{ include.site }} curators maintain a knowledge base of known name changes and aliases for scientists in our database. That is what gets consulted in the next step, where we might discover that `adamčuk, peter` has also published as `adamčuk, piotr` and was previously known as `adamčuková, petra`, in which case we augment our name search to include the additional variation.

So the parser will tentatively generate a multitude of possible names and spellings and will use them all to search for them. As a way of example, this is what we'll get:

- adamzuk, peter
- adamczuk, peter
- adamčuk, peter
- adamčuk, piotr
- adamčuková, petra

All these names were added because our parser consulted the knowledge base of author names. Our parser doesn't know this is one and the same person; but it has a way of seeing/discovering the chain of name changes. If the knowledge database is correct, which is most of the time, it will be able to start from the user input and arrive at other names. 

Next, we'll use all of the author names discovered so far, and take one step further -- we'll generate all the possible name variations that might be derived from them using abbreviations. For example, an author with a middle name such as `John James Doe` might appear in the scientific literature as `Doe, J.`, `Doe, John`, `Doe, John J.`, and possibly `Doe, John James` and `Doe, John J.`

At query time, the author search will adapt its strategy based on the user input. If for example the user entered `acamczuk, p` then our parser will assume they are looking for any `adamczuk` whose first name starts with "p" (i.e. `adamczuk, p*`), and give them all peters, piotrs, pauls, pans and pons. However, if the user typed `adamczuk, peter` then the search engine will instead return `adamczuk, peter`, `adamczuk, peter <some other name>`, `adamczuk, p`, `adamczuk, p <some other name>` and all of the variations and synonyms thereof (`adamčuk, peter`, `adamčuková, petra`, `adamčuková, petra *`, etc.)

### Conclusions

So what started as a seemingly simple search has, behind the scenes, transformed into a massive and very complicated query. Our implementation of author searches attempts to strike a balance between the desire to be precise, and the desire to be inclusive (recall). The logic is complex, it takes advantage of what {{ include.site }} knows about publishing conventions and supplements it with a curated knowledge base, which we regularly update based on user input.

If an author search produces unexpected results, it usually is because of these reasons:

- the curated knowledge base is too broad or too narrow: i.e. it is missing a synonym, or has a synonym too many -- and joins unrelated names together
- haphazard interferences: the transliterations as implemented mistakenly map distinct author names to the same equivalent ASCII version, and end up retrieving records authored by distinct scientists with similar names

One possible solution to the ambiguity problem is to perform an exact author search, which bypasses the steps described above by prepending the equal sign (`=`) to the author search field, e.g. `=author:"adamčuk, peter"`.