---
layout: blog_post
title: "Updates on ADS Interfaces and the Announcement of Bumblebee"
author: "Alberto Accomazzi"
position: "ADS PI/Project Manager"
category: blog
label: general
thumbnail: img/ads_logo.png
---
<img src="{{ site.baseurl }}/img/ads_logo.png" width="128"><br>
The Astrophysics Data System (ADS) is a tool for finding astronomy and planetary science publications. ADS currently has three different interfaces:

 * [ADS “Classic”](http://adsabs.harvard.edu/abstract_service.html) -- the one you all know and love,
 * [ADS “Labs”](http://adslabs.org/adsabs) or “2.0” -- the first interface to an updated search engine, and
 * [ADS “Bumblebee”](https://ui.adsabs.harvard.edu/#index/) -- currently under active development.


We are very pleased to introduce [Bumblebee](https://ui.adsabs.harvard.edu/#index/)! This interface is in the beta stage of development and is ready for more users. It features a clean look and powerful search and filtering operations but it is indeed a beta and still has some quirks and bugs. However, there are some features which we think you’ll find so useful, we want to tell you about them as soon as possible. Over the next couple months, we plan to highlight some of these features in a series of blog posts, so stay tuned!

The search engine that powers  Bumblebee enables faster and more complex searches than Classic. Classic is well suited for things like finding articles by author or title, but it lacks the ability to examine citations, search full-text, or progressively filter results.  We are incorporating all of the features found in Labs and Classic into Bumblebee and are anticipating that Labs will be deprecated and replaced by Bumblebee by the end of 2015.

Never fear, ADS Classic will remain available and supported for the foreseeable future. However, while bug fixes are being applied, Classic is not undergoing any new development. In the very far distant future, long after you and your postdocs have retired, when Classic is deprecated, all abstract page URLs will remain fully functional and so there will be no broken links and no need to change your links to ADS.

The myADS notification service will remain unchanged for the moment. In the next year or so we expect to provide an even better custom notification service using the same technology which underpins Bumblebee.

If you want to be on the bleeding edge and help us run Bumblebee through the paces, please check out the [Help Pages](http://adsabs.github.io/help/search/) for instructions on how to search and give it a go. We welcome your feedback on Bumblebee via issues on the [Github repo](https://github.com/adsabs/bumblebee/issues), tweets to [@adsabs](https://twitter.com/adsabs), or email to adshelp@cfa.harvard.edu.

All of Bumblebee's code is [publically accessible on Github](https://github.com/adsabs/bumblebee) and issues and pull requests are always welcome. The API powering Bumblebee is also available to users and we are planning to publish the [documentation](http://adsabs.github.io/help/api/) for it soon. If you would like to develop widgets or applications to interface with ADS services, you can generate an API Key by [creating an account](https://ui.adsabs.harvard.edu/#user/account/register) and navigating to the API Token section in Settings. We are looking forward to future [hack days](http://www.astrobetter.com/blog/tag/hackday/) and seeing what the community builds with these services!
