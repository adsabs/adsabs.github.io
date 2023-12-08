
ADS’s API, or application programming interface, is the service that accepts requests and returns the requested information. For example, when a user searches in ADS, the website sends a search request to the API, which performs the search and returns the results to the website, which formats and displays them to the user.

Early in the development of the new ADS, we decided to make its API more easily accessible and usable for our users, for development of your own tools and scripts. To that end, we’ve created documentation on API usage and examples in the form of [Jupyter notebooks](https://github.com/adsabs/adsabs-dev-api), provided support for users writing their own API scripts, and [advertised third-party tools](../blog/3rd-party-tools) our users have created for our API. Users have responded by building tools to more easily [search ADS within Python](https://ads.readthedocs.io/en/latest/), [maintain](https://github.com/yymao/adstex) [external](https://github.com/pcubillos/bibmanager) [bibliographies](https://github.com/r-xue/ads2bibdesk), and [visualize results](https://github.com/03b8/ads2gephi).

However, while our existing API documentation covered the most widely used features, such as searching ADS and using libraries, there were a number of useful features that we’ve never documented for our user base. And that doesn’t even touch all of the new features we’ve added over the last few years! Instead of updating our existing docs in a piecemeal manner, we decided to document our full API using the [OpenAPI](https://swagger.io/specification/) specification<sup>[1](#footnote1)</sup>.

The OpenAPI spec is a language-agnostic, widely adopted industry standard for documenting APIs in a machine-readable way. We spent weeks documenting and describing 80+ user-facing (and, for internal use, 70+ data pipeline and internal) API operations, resulting in a comprehensive document that combines descriptions, examples, and schema for each operation. This document is now available to explore visually using our new [beautiful, easy to use documentation](../../help/api/api-docs.html)<sup>[2](#footnote1)</sup>.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_apidocs.png" />
<em>New API help documentation</em>
</div>
<br>

Our [new API documentation](../../help/api/api-docs.html) looks a little overwhelming at first, but it’s easy to use once you get the hang of it. First, all of the available operations, or types of API requests, are organized by function in the sidebar on the left. Click on one to see the full description of that operation. To find a specific operation, you can also use the Search bar at the top, scroll through the page (all operations are listed in one long, scrollable list), or use your browser’s "find in page" function. The documentation for each operation includes the endpoint, or operation, itself (e.g. `/search/query`), the [HTTP method](https://www.w3schools.com/tags/ref_httpmethods.asp) to use (e.g. GET), a description of the operation, any required and optional parameters and request bodies, and the possible responses.

This is all very useful already, if similar to the existing Jupyter notebook documentation. Where these docs really shine, though, are with the built-in try-me functionality. To use this, first [get your API key](https://ui.adsabs.harvard.edu/user/settings/token) and copy it into the box in the [Authentication section](../../help/api/api-docs.html#auth) and click Set. Now you can try out the API directly from this documentation! Let’s look at an example.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_auth.png" />
<em>API token authentication box</em>
</div>
<br>

We’ll start with a basic search, using the operation labeled [Search ADS](../../help/api/api-docs.html#get-/search/query). This operation uses the GET method and the endpoint `/search/query`. A longer description, with examples, is also provided in the documentation.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_searchADS.png" />
<em>Search ADS operation</em>
</div>
<br>

Scroll past the description and examples to the Request section. Here, you’ll find a list of required (marked with an asterisk) and optional parameters, each with a short helpful description. For this operation, the only required parameter is the “q” parameter; enter your search terms here. In this example, shown below, we’re searching for papers containing the word “star.” There are also some optional parameters available; here, we’re using the “fl” parameters to specify that we want the bibcode, title, author, and publication date returned for each search result.

Some other things to note about the request parameters section:
* Generally, parameters need to be URL-encoded in an API request, but when running requests via these docs, the page will automatically do the encoding for you. You can use spaces and special characters in your search terms here just as you would when searching on the ADS website, without needing to encode them.
* Below some of the parameters, there’s an example shown; click on the example to fill it in. You can also use the “fill example” button at the bottom of the list of parameters to fill all available examples.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_searchADS-request.png" />
<em>Search ADS request parameters</em>
</div>
<br>

Once you’ve filled in the parameters you’d like, scroll to the end of the parameter list and click Try. This will format your request, send it, and return the results. The request response is shown in the “Response” tab, in JSON format. The “responseHeader” section contains some information about the request, while the “response” section (shown below) contains the actual request results. In this example, 556,985 total results were found, and the page is displaying the first 10 in the Response box.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_searchADS-response.png" />
<em>Search ADS response</em>
</div>
<br>

You can scroll through the search results here, or you can click on the “curl” tab to copy the request formatted using your input parameters to use in your own scripts.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_searchADS-curl.png" />
<em>Search ADS curl command: copy this into your terminal to run the query as formatted</em>
</div>
<br>

This works similarly for operations that have the POST HTTP request method, but there is a slight difference. Let’s look at one more example. The [BibTeX export for multiple bibcodes](../../help/api/api-docs.html#post-/export/bibtex) uses the POST method. You can see that while this operation doesn’t have any parameters (though some POST operations do), it does have a request body, which is used to pass in the bibcodes you want to export. The default view for a request body is the “schema” tab, which shows the information you can pass in via the body (again, the fields marked with an asterisk are required).

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_bibtex-post.png" />
<em>BibTeX export for multiple bibcodes</em>
</div>
<br>

To test this operation, click on the “example” tab. It defaults to an empty box; click on “fill example” to fill in the placeholder text that demonstrates the proper formatting.

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_bibtex-post-body.png" />
<em>Request body; click on the Example tab, then "fill example" to show the proper request body formatting</em>
</div>
<br>

Fill in your bibcodes in the placeholder text:

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/blog_2021-08-04_bibtex-post-body-2.png" />
<em>Edit the placeholder request body as necessary</em>
</div>
<br>

Then click the Try button to send the request and receive your results. The response and curl sections are similar to those for the search example above.

And that’s it! If you can follow these two examples, you’re ready to take on anything else in the [documentation](../../help/api/api-docs.html). You can find links to this and to the rest of our API documentation [here](../../help/api/). And we’re not done with our [collection of Jupyter notebooks](https://github.com/adsabs/adsabs-dev-api); we’re working on adding more notebooks with more in depth API examples. As always, email us if you have any questions.  

<br>
<a name="footnote1">1</a>: This work was inspired by an ADS Hack Day project by Diab Jerius ([Github](https://github.com/djerius)).<br>
<a name="footnote2">2</a>: This documentation is powered by [RapiDoc](https://mrin9.github.io/RapiDoc/index.html).
