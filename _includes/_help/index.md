<h2>Welcome to the {{ include.site }} Help Pages</h2>

<p>This site is a place to find <b>documentation</b>, <b>tutorials</b>, and other <b>general information</b> about the {{ include.site }} services. The topics are listed in the <b>left sidebar</b> and the <b>search bar</b> in the upper right can be used to search the entire site.</p>

<p>To view the latest information about the {{ include.site }}, visit the <a href="{{ site.baseurl }}/blog">{{ include.site }} blog</a>.</p>

<p>If you cannot find what you are looking for, please reach out to us at <a href="mailto:{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}">{% if include.site == 'SciX' %}help@scixplorer.org{% else %}adshelp@cfa.harvard.edu{% endif %}</a>.

<br>
<div class="scalable scalable-16-9">
  <div class="scalable-content">
    <iframe src="https://www.youtube.com/embed/i7O7ylHLniI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
</div>
