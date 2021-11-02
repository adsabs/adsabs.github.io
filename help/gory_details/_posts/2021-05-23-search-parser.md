# Search Syntax

The following section describes extra details about the search syntax not found, in otherwise comprehensive, [search syntax help](../../search/_posts/2015-02-09-search-syntax.md)


## Big Picture

The search has two distinct phases:

1. building query
1. executing query, collecting results

The first phase is what we are going to discuss here. We'll break it down further into:

1. parsing text into AST (abstract syntax tree)
1. modifying query tree (semantic parsing)
1. building query object


## Parsing text into AST

The [Search Grammar](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/grammars/ADS.g) defines the search language of ADS. It is a context-free grammar and it is used to generate a client library ([by ANTLR](https://www.antlr.org/))

If you don't like reading EBNF grammars (who does?) you'll find a good explanation of ADS syntax here: [search syntax help](../../search/_posts/2015-02-09-search-syntax.md)

But as a reward for having found this obscure corner of the help, we'll illustrate few more special situations not covered there.

### Operators

The search operators have the following precedence (from more important to less): `NEARx -> NOT -> AND -> OR -> " "`

Some details worth mentioning: 

### Empty space is the default

Better to illustrate it by way of examples:

`jim and john not mary` becomes behind the scenes: `(jim AND (john NOT mary))` because `NOT` has precedence over `AND`

`john jim and mary` becomes `(john AND (jim AND mary))` **right now** and the stress is on **now**; for the time being ADS search defaults to `AND` logic for the search operations. We are returning results that contain all the elements of the query. The reasons for this default behaviour are complex (and for most part obsolete -- more on that later). This behaviour can change in the future; if ADS would default to sorting by relevancy then such a change would be (potentially highly) beneficial.

### You can modify the default operator

It can also be changed on demand -- by adding `q.op=OR` into the search parameter; in which case the logic will change dramatically. For any given query the results will contain many more results, but if sorted by relevancy score, the top items will be still the ones returned with the default `AND` operator.

### ADS supports proximity searches

Yes, many people will not know about it, but you can do stuff like: `dog NEAR5 cat` -- this will find any notition of the barking animal appearing up to 5 positions far/close to the miaowing animal. The query as written will actually be parsed as `title:(dog NEAR5 cat) | body:(dog NEAR5 cat)...` (but that is an unimportant detail for now). The `NEAR` has to be followed by a number [1-5] and it will not care about the order; i.e. `cat NEAR5 dog` == `dog NEAR5 cat` -- this search can be very powerful, especially if applied against fulltext. It can also be quite expensive (computationally) - especially when the search term(s) have synonyms.

### There is no in-order proximity operator, but ADS still supports this feature

ADS has a limited support for **in order proximity** - if you make a phrase search like so `abs:"newtonian solar"~3` the word `newtonian` (and its synonyms) will have to be followed by `solar` (and its synonyms) for up to 3 positions away. We do not have a special operator for it though; if what you search for has more than 2 words, we'll decide how far apart they can be if you do `abs:"foo bar baz"^3`


### Syntax Parsing

OK, so back to the syntactic parsing -- how does it actually work? We have a formal grammar which describes the query language. Based on that, we have generated a library (in Java) which is included inside SOLR. When SOLR receives the user input, before it can start searching for documents, the user query (string) will be turned into a query object. And that is the objective of the parser. First comes the syntactic phase during which an ANTLR parser will be 'eating` input character by character. It will occassionally veer off to explore a possible (alternative) branch, to either pursure it further or return back and start branching from some previous position. The input has to be syntactically correct, if we explored all possible readings and there are still some input characters left, it means the input is non-conforming and we'll generate an exception and give up.

This is a feature, but it is border-line feature/bug. The syntax parser is `unforgiving` (that is the actual name of the class in Java). It would be possible (and sensible thing to do) to actually first try to parse the input and on failure try again with some less unforgiving parser; but we have never gotten to it -- so perhaps in the future... just know that if the parser encounters an error, it will generate an exception and the exception will actually say why/what has failed.

If the query is correct, however - after the parser finished parsing, we'll have **AST** (Abstract Syntax Tree). A hierarchical datastructure (a tree) instead of the flat chain of characters.

Here an example (it is only illustration, inside the search engine the AST will be richer):

    "(this) (that)" 	->	
                                (DEFOP 
    (CLAUSE (                               (CLAUSE (
        DEFOP (                                 DEFOP (
            MODIFIER (                              MODIFIER (
                TMODIFIER (                             TMODIFIER (
                    FIELD (                                 FIELD (
                        QNORMAL this))))))                      QNORMAL that)))))))


In human words: the input `(this) (that)` has been parsed into `AST`; the tree starts at `DEFOP` node (default operator) which has two children (`CLAUSE`s). Each `CLAUSE` itself is made of strict chain of components: `DEFOP->MODIFIER->TMODIFIER->FIELD` -- they are all empty (with implicit value of none). It is only after we have arrived to a terminus `QNORMAL` that we also see values. Inside the tree, we will have information about every bracket, position, and links to parent/children.

This tree will be further modified in the next phase.


### Semantic Parsing

There is a lot of magic that happens in this next phase. All of it is defined inside [pipeline](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/src/java/org/apache/lucene/queryparser/flexible/aqp/AqpAdsabsNodeProcessorPipeline.java)

Pro tip: if you add `debugQuery=true` to your search request, you'll see the serialized version of the query as parsed by SOLR. For example 


    "debug":{
        "rawquerystring":"abs:\"newtonian solar\"~3",
        "querystring":"abs:\"newtonian solar\"~3",
        "parsedquery":"CustomScoreQuery(custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5))))",
        "parsedquery_toString":"custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5)))",
        ...
    }


Pro tip (II): If you have access to STDOUT/logging of the SOLR instance, you will see LOTS of details; each and every step in the query pipeline produces and output. This information is however only printed to STDOUT. Here is an example:


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


There is over 60 steps inside the pipeline, some of them extremely complex (see for example [author search](./2021-04-26-author-search.md)) and some simple. We cannot describe here everything that happens there; but we should point out that the pipeline is a like a chain of transducers. Each component will see the `AST`, it will modify it and then processing switches to the next component. There are pre- and post- stages; which would correspond to in-order and post-order traversal of the tree. And in some situations the parser will invoke itself, so it is like a coiled snake eating its own tail -- is it messy? Perhaps, but we'd add that it is only as messy as it needs to be. The work done by the parser is extremely important, it is a complicated job of transforming, extending, cutting, slicing and re-constructing the query. It is complicated because it has to be, but it is also very powerful. And it keeps evolving with ADS users and their requests.

## Building Query Object

Once every component had a chance to modify the AST, we practically pruned the tree into almost a flat list of parent/child relationships. At the end of those 60 transducers, we will have a much lighter AST. And this object will be passed to [`query builders`](https://github.com/romanchyla/montysolr/blob/master/contrib/adsabs/src/java/org/apache/lucene/queryparser/flexible/aqp/AqpAdsabsQueryTreeBuilder.java). Their job is to turn this modified semantic tree into **query objects** as understood by Lucene/SOLR. That `Query` object will be responsible for selecting **and** scoring documents based on the users input and the query parameters that came with it or were presented by default.

Majority of those query objects are typical Lucene/SOLR citizens such as `BooleanQuery`, `TermQuery` etc. There is fbut we can say that during the life of ADS few more (specialized) categories were added. Some of these will receive a special treatment in here as well:

    - BitSetQuery: allows ADS users to select documents based on the list of IDs (this supports very large number of identifiers; millions of them)
    - SecondOrderQuery[2021-08-06-second-order-query.md]


## Special Parameters Affecting Search

There is plethora of options that will affect how the search is executed, many of them are described directly in the [SOLR documentation](https://solr.apache.org/guide/7_3/common-query-parameters.html)

Here are some ADS specific ones that can be changed:

### aqp.unfielded.tokens.strategy

Possible values: tag, join, add, multiply, **disjuncts**

This controls how we are going to generate additional queries for an unfielded search (i.e. search which omits index information such as `author:huchra nasa`)

Our parser is not smart (slow) enough to see that `nasa` is not a name, so when it see this `unfielded` part of the query, it can do the following:

    - tag: produces no query changes, but the unfielded tokens can be seen/used by other components to generate/modify query object
    - join: will join the unfielded portion of the query to its prefix effectively saying `author:"huchra nasa"` (especially when **aqp.unfielded.tokens.new.type** is phrase)
    - add: will construct additional query with the ambiguous part of the query being searched separately, e.g. (`author:"huchra nasa"` OR `+author:huchra +nasa)`
    - multiply: this is very similar to the `add` strategy but the difference is in how the resulting query gets parsed; in here we are not constructing query objects directly but instead we'll re-parse the newly constructed query from the string up and therefore we can apply the whole query parsing/building logic to just portion of the query; the new parser will start from analyzing `author:huchra nasa author:\"huchra nasa\"`
    - disjuncts: this is like the `multiply` strategy but instead of adding OR clauses, we will generate a disjunct query which affects scoring. Only the highest scoring portion of the query affects final score, thus if we programmatically added something to the user's input or not, it will not artifically inflate the final score

### aqp.unfielded.tokens.new.type

Can be combined with the parameter above, affects what happens to the identified unfielded portion of the query.

    - simple: tokens are joined together by a white space
    - phrase: AST tokens are joined together to produce a phrase AST
    - normal: AST tokens are joined together into an AST group (as if the user typed: `(foo bar baz)` - i.e. with explicit quotes)

### aqp.unfielded.tokens.function.name

A function that will be used to reparse the unfielded portion of the query; only applicable for `multiply` and `disjuncts` strategies. For the list of available functions/operators, see: [query functions](2021-08-07-query-functions.md). The default is `edismax_combined_aqp`


### aqp.defaultOperator

By default, ADS will search using 'AND' operator. But if modified (the only sensible option is probably 'OR') then this will make the search engine evaluate every search parameters as 'nice to have'. This is actually better than it sounds, because when sorting search results by score, the results are coming with score computed by relevancy (which is the secret sauce that changes so it cannot be described; but users might find the relevancy score to be much better than the ADS defaults)


### aqp.unfieldedSearch

By default, this is the list of fields that get searched when no field is specified: `author^1.5 title^1.4 abstract^1.3 all` -- obviously, one could modify this using a url parameter.



### aqp.force.fuzzy.phrases

author,first_author,book_author,editor