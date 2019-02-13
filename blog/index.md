---
layout: blog_page
---
# ADS Blog
[Sign up](http://eepurl.com/ggoxhn) for our monthly email updates.

<div class="container">
    <div class="row">

{% for post in site.posts %}

    {% if post.category contains 'blog' %}

      <div class="panel panel-default">

        <div class="panel-body">

            <div class="col-md-2">
                {% if post.thumbnail %}
                    <img src="{{ site.baseurl }}/{{ post.thumbnail }}" style="max-width: 340px;height:auto"/>
                {% else %}
                    <img src="{{ site.baseurl }}/img/ads_logo.png" style="max-width: 340px;height:auto"/>
                {% endif %}
            </div>

            <div class="col-md-2"></div>

            <div class="col-md-8">
                <h2>
                    <a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a><br><small>{{ post.date | date_to_string }}</small>
                </h2>

                <p>
                    {{ post.content | strip_html | truncatewords:40 }}
                </p>
            </div>

        </div>

        <div class="panel-footer">

            <span class="label label-success">
                author: {{ post.author }}
            </span>
            &nbsp;
            <span class="label label-primary">
                category: {{ post.label }}
            </span>

        </div>



      </div>

    {% endif %}

{% endfor %}
</div>
</div>
