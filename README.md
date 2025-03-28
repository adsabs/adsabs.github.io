# ADS Help and Blog pages

Static web pages that serve the help and blog pages of the NASA/SAO Astrophysics Data System.

#### Current pages
  * [View the help pages](https://ui.adsabs.harvard.edu/help/)
  * [View the blog pages](https://ui.adsabs.harvard.edu/blog/)

#### Updating the help pages

All the help pages can be found under the folder `help`. To add new content, you will have to read about how jekyll's [layout system works](http://jekyllrb.com/docs/structure/). A quick way to add content is to:

  1. Add a new folder, eg., `help/my_help/`
  2. Add a landing page, eg., `help/my_help/index.md`
  3. Add a `_posts` folder, eg., `help/my_help/_posts`
  4. Add a post, eg., `help/my_help/_posts/2015-10-10_my_first_post.md`

You can now access your help pages at `http://localhost:4000/help/my_help/` which loads the `index.md`, and any relevant content that it references within `2015-10-10_my_first_post.md` can be added to the index.

If making a pull request, follow the rules described in `CONTRIBUTING.md`.

#### Adding a category
Unfortunately if you add a new category (e.g. "search", "actions", "userpreferences"), you need to do some configuration beyond
adding the folder with the category name, with an index.html and _posts folder.
You also need to add some markup to _includes/left-nav.html (use the previous accordion divs as a template).


#### Contributing a blog post

All the blogs are kept under the folder `blog/_posts/`. The following rules must be kept to when making a blog post:

  1. Name the file with `DATE_NAME`.md, eg., `2015-10-10_my_post.md`
  2. Within the file, you must include the following content at the top of the file:

    ```
    ---
    layout: blog_post
    title: "Title of your blog"
    author: "Author of your blog"
    position: "Job position of author"
    category: blog
    label: general
    thumbnail: blog/images/blog_DATE_thumbnail.png
    ---
    ```
    * `layout`: leave as blog_post
    * `title`: modify to your needs
    * `author`: modify to your needs
    * `position`: modify to your needs
    * `category`: leave as blog
    * `label`: this can be a string, or list. Allowed values: 'general', 'technical', 'news'. The choice of label will decide where it is viewed within the blog.
    * `thumbail`: path to the thumbnail, assumes its within the git repository

For more information on formatting within jekyll you can read [here](http://jekyllrb.com/docs/posts/), or any other places that has information about markdown. Markdown can also render HTML if you prefer to write using that.

If you wish to see the content you are writing while working in markdown, the recommended tool as of October 2017 is
[grip](https://github.com/joeyespo/grip).  Other ones we have considered/used in the past are [dillinger.io](http://dillinger.io/) or some programs such as [haroopad](http://pad.haroopress.com/).

If making a pull request, follow the rules described in `CONTRIBUTING.md`.

#### For development

The help pages are static web pages built using Jekyll (written in Ruby) and taking advantage of GitHub's support of Jekyll. To run locally, first install Ruby, then Jekyll, a Ruby Gem. The recommended method is following the instructions on the Jekyll site:

* [Main installation page](https://jekyllrb.com/docs/installation/)
* [MacOS instructions](https://jekyllrb.com/docs/installation/macos/)

After installing Jekyll, run the following commands to preview the site:

* install gems with `bundle install` (you may need to run `bundle update` first to update the Gemfile.lock file
* build with `jekyll build`
* serve the project with the command `jekyll serve`

You will now be able to access the help pages locally at `http://0.0.0.0:4000`  or `localhost:4000` (default configuration). After the website is built for the first time, you should only need to save the file, wait a second or two for it to rebuild automatically (check the terminal window where you ran `jekyll serve`), then refresh the page to see any changes.

### Maintainer

Mugdha
