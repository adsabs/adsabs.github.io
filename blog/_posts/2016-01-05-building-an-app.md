---
layout: blog_post
title: "Wrecipe for Simple ADS Apps"
author: "ADS Team"
position: "ADS Developers"
category: blog
label: technical
thumbnail: blog/images/blog_2016-01-13_thumb.jpg
---

Underneath the new user interface of the ADS, ADS Beta (or Bumblebee), there is the rebuilt infrastructure of the ADS platform that serves the application layer of the ADS. At the start of last year, we made these services accessesible to the community via an API, for personal use, to build apps for themselves, their departments, or even the community as a whole. During the recent 227th Meeting of the American Astronomical Society, we decided to build a simple application for the Hack Day, to demonstrate the ease at which you can create and deploy an application that makes use of the data available at the ADS.

*Warning: this post becomes more technical, and overly uses a Wrestling theme.*

The following is needed for the recipe:

  1. ADS API key (make a username here, and then go to User Settings -> Customize -> API Token)
  2. A Herokuapp account (visit herokuapp.com)
  3. Python "unofficial ADS client" by Andy Casey (https://github.com/andycasey/ads)

### Step 1: Decide what your application should do

We decided to create an application that pits two authors against one another, by comparing their publication metrics against each other, and to utilise a wrestling theme. Make a quick design plan:


### Step 2: Obtain the information you need from the ADS

One possible approach is to just compare total citations of one author to another, but obviously this can lead to biases given that someone who works longer should have more citations, people who have more papers from collaborations will have more citations, etc. To get around this annoyance, we chose to use the RIQ, a metric that is meant to *fairly* compare two authors. You can read more about this metric here. Of course, there are problems with this metric too, but this application is meant to demonstrate the API, not give a tool to use for serious work.

To obtain the RIQ for authors, first we need to get the list of bibcodes of a specific author:

```python
>>> import ads
>>> ads.TOKEN = 'ADS_API_TOKEN_THAT_I_WILL_NOT_COMMIT_TO_GITHUB'
>>> solr_query = ads.SolrQuery(q='Elliott, J.', fl=['id', 'bibcode'])
>>> bibcodes = [paper.bibcode for paper in solr_query]
```

This gives us all the bibcodes for author "J. Elliott", and requests for the field items "id" and "bibcode" to be returned, which ensures that no lengthy requests are carried out by our search engine. For example, if you request `fl=['citations']`, this will carry out a second order operation, which will make the response slower.


Once you have the relevant bibcodes, we need to ask the metrics end point for the metrics for the list of papers:

```python
>>> metrics_query = ads.MetricsQuery(bibcodes=bibcodes)
>>> metrics_response = metrics_query.execute()
>>> riq = metrics_response['indicators']['riq]
>>> print riq
40
```

The above is also so simple, you could do it via curl requests as outlined in our help pages, or write your own client in the language of your choice.

### Step 3: Serve your logic in a web app
s
Our application will receive two authors names, and return the RIQs of each author, which will then display the winner (and loser) on the front-end application. To do this, we built a back-end application using Python-Flask, and a front-end application written in JavaScript.

The Flask application will have an end point that returns the RIQs of each user, and an end point that serves the static content of the front end application written in JavaScript, which can be seen in a few lines of code.

The JavaScript application

### Step 4: Put the application on a free-service

You can opt to host your application locally if you prefer, and there are a plethora of free options on the internet. One way is to place your 

*Note* If you use your own API token for an application that is available to other users, your rate limits will be consumed as normal, and may run out during a 24 hour period. If you believe your application deserves its own rate limits then feel free to tweet us [@adsabs](http://twitter.com/adsabs) or [contact us directly](adshelp@cfa.harvard.edu)