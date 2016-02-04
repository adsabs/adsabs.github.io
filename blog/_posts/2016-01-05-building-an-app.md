---
layout: blog_post
title: "Wrecipe for Simple ADS Apps"
author: "ADS Team"
position: "ADS Developers"
category: blog
label: technical
thumbnail: blog/images/blog_2016-01-13_thumb.jpg
---

Underneath the new user interface of the ADS, ADS Beta (or Bumblebee), there is the rebuilt infrastructure of the ADS platform that serves the application layer of the ADS. At the start of last year, we made these services accessesible to the community via an API, for personal use, to build apps for themselves, their departments, or even the community as a whole. During the recent 227th Meeting of the American Astronomical Society, we decided to build a simple application for the Hack Day to demonstrate the ease at which you can create and deploy an application that makes use of the data available at the ADS.

*FYI: this is more technical, and repetively uses a cooking/Wrestling theme.*

### Ingredients
The following is needed for the wrecipe:

  1. An ADS account and an ADS API key (make an account [here](https://ui.adsabs.harvard.edu/#user/account/register), and then go to User Settings -> Customize -> API Token)
  2. A [Heroku account](http://herokuapp.com)
  3. Python "unofficial ADS client" by Andy Casey (https://github.com/andycasey/ads)

### Step 1: Decide what your application should do

First, we decided to create an application that pits two authors against one another by comparing their publication metrics against each other. Second, apply the 90s-00s WWE/WWF theme.

![WWF](blog_2016-02-04_image02.jpg)

### Step 2: Obtain the information you need from the ADS

We wanted to compare two authors against each other, *reasonably* fairlyOne possible approach is to just compare total citations of one author to another, but obviously this can lead to biases given that someone who works longer should have more citations, people who have more papers from collaborations will have more citations, etc. To get around this, we chose to use the RIQ, a metric that is meant to *fairly* compare two authors. You can read more about this metric [here](https://ui.adsabs.harvard.edu/#abs/2012PLoSO...746428P/abstract). Of course, there are problems with this metric too, but.....

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

The above is fairly simple, and so you could do it via curl requests as outlined in our help pages, or write your own client in the language of your choice.

### Step 3: Serve your logic in a web app

Our application will receive two authors names, and return the RIQs of each author, which will then display the winner (and loser) on the front-end application. To do this, we built a back-end application using Python-Flask, and a front-end application written in JavaScript. If you want to see the full code, you can see it [here](https://github.com/jonnybazookatone/authorsmackdown). At this stage you can utilise your favourite web application, cgi-bins, ruby on rails, go-lang, etc.

### Step 4: Give your app to the public

You can opt to host your application locally if you prefer, and there are a plethora of free options on the internet. To get things running quickly, we chose to host our application on Heroku app (http://herokuapp.com). You only need to do two things:

  1. Configure your heroku app as outlined on Heroku
  2. Supply your `API_DEV_KEY` via Heroku config

*Note* If you use your own API token for an application that is available to other users, your rate limits will be consumed as normal, and may run out during a 24 hour period. If you believe your application deserves its own rate limits then feel free to tweet us [@adsabs](http://twitter.com/adsabs) or [contact us directly](adshelp@cfa.harvard.edu)

### Step 5: Put it in the oven

![Oven](blog/images/blog_2016-02-04.jpg)

