{% if include.ads %}The following page describes extra details about the search syntax not found in the otherwise comprehensive [search syntax help](search-syntax).


## Big Picture

The search has two distinct phases:

1. building query
1. executing query, collecting results

The first phase is what we are going to discuss here. We'll break it down further into:

1. parsing text into the AST (abstract syntax tree)
1. modifying the query tree (semantic parsing)
1. building the query object


## Parsing text into AST

The [Search Grammar](https://github.com/adsabs/montysolr/blob/main/montysolr/src/main/antlr/ADS.g) defines the search language of {{ include.site }}. It is a context-free grammar and it is used to generate a client library ([by ANTLR](https://www.antlr.org/)).

If you don't like reading context-free computer grammars (who does?) you'll find a good explanation of {{ include.site }} syntax here: [search syntax help](search-syntax).

But as a reward for having found this obscure corner of the help, we'll illustrate a few more special situations not covered there.

### Operators

The search operators have the following precedence (from higher to lower priority): `NEARx -> NOT -> AND -> OR -> " "`

Some details worth mentioning: 

**Empty space is the default** 

Better to illustrate it by way of examples:

`jim and john not mary` becomes behind the scenes: `(jim AND (john NOT mary))` because `NOT` has precedence over `AND`. But `john jim and mary` becomes `(john AND (jim AND mary))` because `AND` operator has precedence over empty space (operator) -- notice how `jim and mary` is evaluated as a group: i.e. the query is **not** parsed as `john AND jim AND mary`. That is a behaviour **right now** and the stress is on **now**; for the time being {{ include.site }} search defaults to `AND` logic for the search operations. We are returning results that contain all the elements of the query. The reasons for this default behaviour are complex (and for the most part obsolete -- more on that later). This behaviour can change in the future if {{ include.site }} switches to a different default operator (`OR`) and makes sorting by relevancy the default sort order. Such a change would be (potentially highly) beneficial but would also change the order of how things get parsed. To make it clearer, if we ever change the default operator to (e.g.) `OR` - then `john jim and mary` will be evaluated as `(jim OR (john AND mary))`

**You can modify the default operator**

It can also be changed on demand by adding `q.op=OR` into URL parameters (i.e. NOT inside the search form), in which case the logic will change dramatically. For any given query the results will contain many more records, but if sorted by relevancy score, the top items will be still the ones returned with the default `AND` operator.

**{{ include.site }} supports proximity searches**

Yes, many people may not know about it, but you can do stuff like: `title:(dog NEAR5 cat)` -- this will find any mention of the barking animal appearing up to 5 words (tokens) from the meowing animal. The `NEAR` has to be followed by a number [1-5] and it will not care about the order; i.e. `cat NEAR5 dog` == `dog NEAR5 cat` -- this search can be very powerful, especially if applied against fulltext. It can also be quite expensive (computationally) - especially when the search term(s) have synonyms.

**There is no in-order proximity operator, but {{ include.site }} still supports this feature**

{{ include.site }} has a limited support for **in-order proximity** - if you make a phrase search like so `abs:"newtonian solar"~3` the word `newtonian` (and its synonyms) will have to be followed by `solar` (and its synonyms) for up to 3 positions away. We do not have a special operator for it though; if what you search for has more than 2 words, we'll decide how far apart they can be. For example if you do `abs:"one two three"~3` then `one` may be 3 words away from `two three` (and it doesn't matter that there are really 4 tokens between `one` and `three`).


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

There is a lot of magic that happens in this next phase. All of it is defined inside the [pipeline](https://github.com/adsabs/montysolr/blob/main/montysolr/src/main/java/org/apache/lucene/queryparser/flexible/aqp/AqpAdsabsNodeProcessorPipeline.java).

Pro tip: if you add `debugQuery=true` to your search request URL parameters (and look at the data as returned by our API), you'll see the serialized version of the query as parsed by SOLR. For example 


    "debug":{
        "rawquerystring":"abs:\"newtonian solar\"~3",
        "querystring":"abs:\"newtonian solar\"~3",
        "parsedquery":"CustomScoreQuery(custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5))))",
        "parsedquery_toString":"custom(abstract:\"syn::newton syn::solar\"~3 title:\"syn::newton syn::solar\"~3 keyword:\"syn::newton syn::solar\"~3, sum(float(cite_read_boost),const(0.5)))",
        ...
    }


Pro tip (II): If you had access to STDOUT/logging of the SOLR instance, you would see LOTS of details; each and every step in the query pipeline produces output. This information is however only printed to STDOUT - and so only {{ include.site }} engineers can really see it.{% endif %}
