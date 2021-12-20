---
layout: post
title: "(Advanced) Search Syntax"
order: 7
---


The following page describes extra details about the search syntax not found in the otherwise comprehensive [search syntax help](search-syntax).


## Big Picture

The search has two distinct phases:

1. building query
1. executing query, collecting results

The first phase is what we are going to discuss here. We'll break it down further into:

1. parsing text into the AST (abstract syntax tree)
1. modifying the query tree (semantic parsing)
1. building the query object


## Parsing text into AST

The [Search Grammar](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/grammars/ADS.g) defines the search language of ADS. It is a context-free grammar and it is used to generate a client library ([by ANTLR](https://www.antlr.org/)).

If you don't like reading context-free computer grammars (who does?) you'll find a good explanation of ADS syntax here: [search syntax help](search-syntax).

But as a reward for having found this obscure corner of the help, we'll illustrate a few more special situations not covered there.

### Operators

The search operators have the following precedence (from more important to less): `NEARx -> NOT -> AND -> OR -> " "`

Some details worth mentioning: 

**Empty space is the default** 

Better to illustrate it by way of examples:

`jim and john not mary` becomes behind the scenes: `(jim AND (john NOT mary))` because `NOT` has precedence over `AND`. But `john jim and mary` becomes `(john AND (jim AND mary))` because `AND` operator has precedence over empty space (operator) -- notice how `jim and mary` is evaluated as a group: i.e. the query is **not** parsed as `john AND jim AND mary`. That is a behaviour **right now** and the stress is on **now**; for the time being ADS search defaults to `AND` logic for the search operations. We are returning results that contain all the elements of the query. The reasons for this default behaviour are complex (and for the most part obsolete -- more on that later). This behaviour can change in the future if ADS switches to a different default operator (`OR`) and makes sorting by relevancy the default sort order. Such a change would be (potentially highly) beneficial but would also change the order of how things get parsed. To make it clearer, if we ever change the default operator to (e.g.) `OR` - then `john jim and mary` will be evaluated as `(jim OR (john AND mary))`

**You can modify the default operator**

It can also be changed on demand by adding `q.op=OR` into URL parameters (i.e. NOT inside the search form), in which case the logic will change dramatically. For any given query the results will contain many more results, but if sorted by relevancy score, the top items will be still the ones returned with the default `AND` operator.

**ADS supports proximity searches**

Yes, many people may not know about it, but you can do stuff like: `title:(dog NEAR5 cat)` -- this will find any mention of the barking animal appearing up to 5 words (tokens) from the meowing animal. The `NEAR` has to be followed by a number [1-5] and it will not care about the order; i.e. `cat NEAR5 dog` == `dog NEAR5 cat` -- this search can be very powerful, especially if applied against fulltext. It can also be quite expensive (computationally) - especially when the search term(s) have synonyms.

**There is no in-order proximity operator, but ADS still supports this feature**

ADS has a limited support for **in-order proximity** - if you make a phrase search like so `abs:"newtonian solar"~3` the word `newtonian` (and its synonyms) will have to be followed by `solar` (and its synonyms) for up to 3 positions away. We do not have a special operator for it though; if what you search for has more than 2 words, we'll decide how far apart they can be. For example if you do `abs:"one two three"~3` then `one` may be 3 words away from `two three` (and it doesn't matter that there are really 4 tokens between `one` and `three`).


### Syntax Parsing

OK, so back to the syntactic parsing -- how does it actually work? We have a formal grammar which describes the query language. Based on that, we have generated a library (in Java) which is included inside SOLR, our search engine. When SOLR receives the user input, before it can start searching for documents, the user query (string) will be turned into a query object. And that is the objective of the parser. First comes the syntactic phase during which an ANTLR parser will be 'eating' input character by character. It will occassionally veer off to explore a possible (alternative) branch, to either pursue it further or return back and start branching from some previous position. The input has to be syntactically correct; if we explored all possible readings and there are still some input characters left, it means the input is non-conforming and we'll generate an exception and give up.

This is a feature, but it is borderline feature/bug. The syntax parser is `unforgiving` (that is the actual name of the class in Java). It would be possible (and the sensible thing to do) to actually first try to parse the input and on failure try again with some less unforgiving parser; but we have never gotten to it -- so perhaps in the future... just know that if the parser encounters an error, it will generate an exception and the exception will actually say why/what has failed.

If the query is correct, however, after the parser is finished parsing, we'll have the **AST** (Abstract Syntax Tree): a hierarchical datastructure (a tree) instead of the flat chain of characters.

Here an example (it is only an illustration, inside the search engine the AST will be richer):

    "(this) (that)" 	->	
                                (DEFOP 
    (CLAUSE (                               (CLAUSE (
        DEFOP (                                 DEFOP (
            MODIFIER (                              MODIFIER (
                TMODIFIER (                             TMODIFIER (
                    FIELD (                                 FIELD (
                        QNORMAL this))))))                      QNORMAL that)))))))


In human words: the input `(this) (that)` has been parsed into an `AST`; the tree starts at a `DEFOP` node (default operator) which has two children (`CLAUSE`s). Each `CLAUSE` itself is made of a strict chain of components: `DEFOP->MODIFIER->TMODIFIER->FIELD` -- they are all empty (with implicit value of none). It is only after we have arrived to a terminus `QNORMAL` that we also see values. Inside the tree, we will have information about every bracket, position, and links to parent/children.

This tree will be further modified in the next phase.


### Semantic Parsing

There is a lot of magic that happens in this next phase. All of it is defined inside the [pipeline](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/src/java/org/apache/lucene/queryparser/flexible/aqp/AqpAdsabsNodeProcessorPipeline.java).

Pro tip: if you add `debugQuery=true` to your search request URL parameters (and look at the data as returned by our API), you'll see the serialized version of the query as parsed by SOLR. For example 


    "debug":{
        "rawquerystring":"abs:\"newtonian solar\"~3",
        "querystring":"abs:\"newtonian solar\"~3",
        "parsedquery":"CustomScoreQuery(custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5))))",
        "parsedquery_toString":"custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5)))",
        ...
    }


Pro tip (II): If you had access to STDOUT/logging of the SOLR instance, you would see LOTS of details; each and every step in the query pipeline produces output. This information is however only printed to STDOUT - and so only ADS engineers can really see it. Here is an example:


     57. step class org.apache.lucene.queryparser.flexible.standard.processors.MultiTermRewriteMethodProcessor
     Tree changed: NO

    --------------------------------------------
     58. step class org.apache.lucene.queryparser.flexible.aqp.processors.AqpGroupQueryOptimizerProcessor
     Tree changed: YES
     Tags changed: YES
     -----------------
    abstract:newtonian : {token_type_attribute=word, max_branch_size=2}
    abstract:syn\:\:newton : {token_type_attribute=SYNONYM, max_branch_size=2}
    abstract:solar : {token_type_attribute=word, max_branch_size=2}
    abstract:syn\:\:solar : {token_type_attribute=SYNONYM, max_branch_size=2}
    title:newtonian : {token_type_attribute=word, max_branch_size=2}
    title:syn\:\:newton : {token_type_attribute=SYNONYM, max_branch_size=2}
    title:solar : {token_type_attribute=word, max_branch_size=2}
    title:syn\:\:solar : {token_type_attribute=SYNONYM, max_branch_size=2}
    keyword:newtonian : {token_type_attribute=word, max_branch_size=2}
    keyword:syn\:\:newton : {token_type_attribute=SYNONYM, max_branch_size=2}
    keyword:solar : {token_type_attribute=word, max_branch_size=2}
    keyword:syn\:\:solar : {token_type_attribute=SYNONYM, max_branch_size=2}
        -----------------
    <boolean operation='or'>
    <slop value='4'>
    <multiPhrase>
    <field start='5' end='14' field='abstract' text='newtonian'/>
    <field start='5' end='14' field='abstract' text='syn::newton'/>
    <field start='15' end='20' field='abstract' text='solar'/>
    <field start='15' end='20' field='abstract' text='syn::solar'/>
    </multiPhrase>
    </slop>
    <slop value='4'>
    <multiPhrase>
    <field start='5' end='14' field='title' text='newtonian'/>
    <field start='5' end='14' field='title' text='syn::newton'/>
    <field start='15' end='20' field='title' text='solar'/>
    <field start='15' end='20' field='title' text='syn::solar'/>
    </multiPhrase>
    </slop>
    <slop value='4'>
    <multiPhrase>
    <field start='5' end='14' field='keyword' text='newtonian'/>
    <field start='5' end='14' field='keyword' text='syn::newton'/>
    <field start='15' end='20' field='keyword' text='solar'/>
    <field start='15' end='20' field='keyword' text='syn::solar'/>
    </multiPhrase>
    </slop>
    </boolean>
    --------------------------------------------
     59. step class org.apache.lucene.queryparser.flexible.aqp.processors.AqpOptimizationProcessor
     Tree changed: NO


There are over 60 steps inside the pipeline, some of them extremely complex (see for example [author search](author-search)) and some simple. We cannot describe here everything that happens there; but we should point out that the pipeline is like a chain of transducers. Each component will see the `AST`, it will modify it and then processing switches to the next component. There are pre- and post- stages; which would correspond to in-order and post-order traversal of the tree. And in some situations the parser will invoke itself, so it is like a coiled snake eating its own tail -- is it messy? Perhaps, but we'd add that it is only as messy as it needs to be. The work done by the parser is extremely important, it is a complicated job of transforming, extending, cutting, slicing and re-constructing the query. It is complicated because it has to be, but it is also very powerful. And it keeps evolving with ADS users and their requests.

## Building Query Object

Once every component has finished modifying the AST, we had pruned the tree into almost a flat list of parent/child relationships. At the end of those 60 transducers, we have a much lighter AST. This object is passed to [`query builders`](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/src/java/org/apache/lucene/queryparser/flexible/aqp/AqpAdsabsQueryTreeBuilder.java). Their job is to turn this modified semantic tree into **query objects** as understood by Lucene/SOLR. That `Query` object is then responsible for selecting **and** scoring documents based on the users input and the query parameters that came with it or were presented by default.

The majority of those query objects are typical Lucene/SOLR citizens such as `BooleanQuery`, `TermQuery`. During the life of ADS a few more (specialized) categories have been added, e.g:

- BitSetQuery: allows ADS users to select documents based on the list of IDs (this supports a very large number of identifiers; millions of them)
- [SecondOrderQuery](second-order)


## Special Parameters Affecting Search

There is a plethora of options that will affect how the search is executed, many of them are described directly in the [SOLR documentation](https://solr.apache.org/guide/7_3/common-query-parameters.html).

Here are some ADS specific ones that can be changed:

### aqp.unfielded.tokens.strategy

Possible values: tag, join, add, multiply, **disjuncts**

This controls how we are going to generate additional queries for an unfielded search (i.e. search which omits index field information such as `author:huchra nasa`)

Our parser is not smart (slow) enough to see that `nasa` is not a name, so encountering this `unfielded` part of the query, it can do the following under these circumstances:

- tag: produces no query changes, but the unfielded tokens can be seen/used by other components to generate/modify query object
- join: will join the unfielded portion of the query to its prefix effectively saying `author:"huchra nasa"` (especially when **aqp.unfielded.tokens.new.type** is phrase)
- add: will construct an additional query with the ambiguous part of the query being searched separately, e.g. (`author:"huchra nasa"` OR `+author:huchra +nasa)`
- multiply: this is very similar to the `add` strategy but the difference is in how the resulting query gets parsed; here we are not constructing query objects directly but instead we'll re-parse the newly constructed query from the string up and therefore we can apply the whole query parsing/building logic to just a portion of the query; the new parser will start from analyzing `author:huchra nasa author:\"huchra nasa\"`
- disjuncts: our default, this is like the `multiply` strategy but instead of adding OR clauses, we will generate a disjunct query which affects scoring. Only the highest scoring portion of the query affects the final score, thus if we programmatically added something to the user's input or not, it will not artifically inflate the final score

### aqp.unfielded.tokens.new.type

Can be combined with the parameter above; affects what happens to the identified unfielded portion of the query.

- simple: our default, tokens are joined together by a white space
- phrase: AST tokens are joined together to produce a phrase AST
- normal: AST tokens are joined together into an AST group (as if the user typed: `(foo bar baz)` - i.e. with explicit quotes)


### aqp.unfielded.tokens.function.name

A function that will be used to reparse the unfielded portion of the query; only applicable for `multiply` and `disjuncts` strategies. For the list of available functions/operators, see: [query functions](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/src/java/org/apache/lucene/queryparser/flexible/aqp/builders/AqpAdsabsSubQueryProvider.java). The default is `edismax_combined_aqp`.


### aqp.defaultOperator

By default, ADS will search using the `AND` operator when two search terms are joined only by a space. But if modified (the only sensible option is probably `OR`) then this will make the search engine evaluate every search parameter as 'nice to have'. This is actually better than it sounds, because when sorting search results by score, they will come back ordered by relevancy score (which is the secret sauce that changes so it cannot be described; but users might find the relevancy score to be much better than the ADS defaults).


### aqp.unfieldedSearch

By default, this is the list of fields, with their weights, that get searched when no field is specified: `author^1.5 title^1.4 abstract^1.3 all` -- obviously, one could modify this using a URL parameter.



### aqp.force.fuzzy.phrases

`author,first_author,book_author,editor` -- these fields, when searched as "some other"~2, will be searched using fuzzy logic.