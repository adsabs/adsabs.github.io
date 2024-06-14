---
layout: post
title: "How to Optimize SciX for Writing a Grant Proposal"
order: 1 
category: learn
---

# Step 1: Search for a paper about a specific topic

### Search for papers about AGN
{% capture query %}
abs:"active galactic nuclei"
{% endcapture %}
{% include_relative _blocks/search-bar-embed.html 
    content=query 
    url="https://scixplorer.org/search?q=abs%3A%22active+galactic+nuclei%22&sort=score+desc%2Cdate+desc&p=1&n=10" 
%}

### Constrain searches for refereed papers about AGN in dwarf galaxies
{% capture query %}
abs:"active galactic nuclei" AND abs:"dwarf galaxies AND property:refereed"
{% endcapture %}
{% include_relative _blocks/search-bar-embed.html 
    content=query 
    url="https://scixplorer.org/search?q=abs%3A%22active+galactic+nuclei%22+AND+abs%3A%22dwarf+galaxies%22+AND+property%3Arefereed&sort=score+desc%2Cdate+desc&p=1" %}

# Step 2: Add useful paper to a new library
{% include_relative _blocks/add-papers-to-library.html %}

# Step 3: Search for a paper similar to another interesting paper
### Use the similar operator on the bibcode identifier of any paper you find interesting
{% capture query %}
similar("2024MNRAS.528.5252M”)
{% endcapture %}
{% include_relative _blocks/search-bar-embed.html 
    content=query 
    url="https://scixplorer.org/search?q=similar(%222024MNRAS.528.5252M%E2%80%9D)&sort=score+desc%2Cdate+desc&p=1&n=10" %}

### Search for the top 10 papers related to the abstract of an interesting paper
{% capture query %}
similar(bibcode: "2024MNRAS.528.5252M”, abstract, 10)
{% endcapture %}
{% include_relative _blocks/search-bar-embed.html 
    content=query 
    url="https://scixplorer.org/search?q=similar(bibcode%3A+%222024MNRAS.528.5252M%E2%80%9D%2C+abstract%2C+10)&sort=score+desc%2Cdate+desc&p=1&n=10" %}

# Step 4: Search for review papers about a topic
{% capture query %}
reviews("active galactic nuclei in dwarf galaxies")
{% endcapture %}
{% include_relative _blocks/search-bar-embed.html 
    content=query 
    url="https://scixplorer.org/search?q=reviews(%22active+galactic+nuclei+in+dwarf+galaxies%22)&sort=score+desc%2Cdate+desc&p=1&n=10" %}

# Step 4: Export citations from Library via UI
{% include_relative _blocks/export-from-library.html %}
 
# OR 

# Step 4: Export citations from Library via API
{% include_relative _blocks/export-from-library-api-embed.html %}
