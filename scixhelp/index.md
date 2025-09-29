---
layout: post_scix
title: 'SciX Help'
no-header: true
---

<div class="help-page">
<h2>Welcome to the SciX Help Pages</h2>

<p>Your comprehensive guide to discovering and managing scientific research. Get started in minutes with our quick start guide below, or use the search bar in the upper right to search the entire site.</p>

<!-- Tabbed Interface -->
<div class="tabbed-interface">
  <div class="tab-navigation">
    <button class="tab-button active" onclick="openTab(event, 'quickstart')">
      <span class="tab-icon"><i class="fa fa-rocket"></i></span>
      Quick Start
    </button>
    <button class="tab-button" onclick="openTab(event, 'api')">
      <span class="tab-icon"><i class="fa fa-code"></i></span>
      API
    </button>
    <button class="tab-button" onclick="openTab(event, 'resources')">
      <span class="tab-icon"><i class="fa fa-compass"></i></span>
      Resources
    </button>
    <button class="tab-button" onclick="openTab(event, 'video')">
      <span class="tab-icon"><i class="fa fa-play-circle"></i></span>
      Video Guide
    </button>
  </div>

  <!-- Quick Start Tab (Default Active) -->
  <div id="quickstart" class="tab-content active">
    <div class="tab-header">
      <h2>Quick Start Guide</h2>
      <p>Get up and running with SciX in minutes. Click any question below to learn how to use our most popular features.</p>
    </div>

<div class="faq-container">
    <div class="faq-item" id="how-to-search">
      <div class="faq-question" onclick="toggleFAQ('faq1')">
        <h3>How do I use SciX?</h3>
        <span class="faq-toggle">+</span>
      </div>
      <div class="faq-answer" id="faq1">
        <p>SciX is a powerful literature search platform that's simple to use. Type any keyword, topic, or author name and hit return for relevant results. For precise results, use targeted search fields:</p>
        
        <ul>
          <li><strong>Basic search:</strong> Searches all record metadata. Type <code>"hurricane"</code> to find 25,000+ records, including papers about hurricanes and papers by authors such as O. Hurricane. Or type <code>"Crutzen"</code>  to find 600+ results by various authors named Crutzen. </li>
          <li><strong>Topic search:</strong> Click abstract + year fields → <code>abs:"hurricane" year:2024-2025</code> → Recent hurricane papers</li>
          <li><strong>Author search:</strong> Click first author + year → <code>first_author:"Crutzen, Paul" year:1990</code> → His 4 first-author papers from 1990</li>
          <li><strong>Collaboration search:</strong> Click author twice + institution → <code>author:"Crutzen" author:"Andreae" inst:"Max Planck"</code> → Their joint Max Planck work</li>
        </ul>
        
        <p>See our <a href="{{ site.baseurl }}/scixhelp/gettingstarted-scix">Getting Started Tutorial</a> for more tips.</p>
      </div>
    </div>
    
    <div class="faq-item" id="create-account">
    <div class="faq-question" onclick="toggleFAQ('faq17')">
      <h3>Do I need an account to use SciX?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq17">
       <p>No, you do not need an account to use SciX. However, there are benefits to creating an account:</p>
       <ul>
         <li><strong>Alerts:</strong> Set up alerts to get updates on your favorite topics, authors, or papers using the bell icon</li>
         <li><strong>Libraries:</strong> Create and manage <a href="{{ site.baseurl }}/scixhelp/libraries-scix">personal libraries</a> to organize your research and share with colleagues</li>
         <li><strong>ORCiD integration:</strong> <a href="{{ site.baseurl }}/scixhelp/orcid-scix">Claim your papers</a> and get guaranteed author matches</li>
         <li><strong>Default discipline settings:</strong> Set your preferred discipline and search result sorting that persist across sessions</li>
         <li><strong>External links:</strong> Easy access to full-text articles and external resources by connecting your library subscriptions</li>
       </ul>
    </div>
  </div>
 
   <div class="faq-item" id="discipline-selection">
    <div class="faq-question" onclick="toggleFAQ('faq16')">
      <h3>How and why would I specify my discipline?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq16">
      <p>Specify your discipline to boost relevant content and improve search results:</p>
      
        <p><strong>Choose discpline from the top-left menu (boosts content):</strong> Select a preferred discipline for your search. Note: "General Science" corresponds primarily to physics, computer science, and chemistry content. This choice doesn't filter out other disciplines but <em>boosts the most relevant content</em> to appear closer to the top of your search results.</p>
      
      <p><strong>Left panel (filters content):</strong> Select a collection by discipline to <strong>filter out results</strong> that don't belong to your selected discipline. This gives you a more focused view of results within your field.</p>
      
      <p><strong>Account benefits:</strong> If you <a href="https://scixplorer.org/user/account/register">create an account</a>, you can select your discipline once and it will stay selected for your future searches until you change it.</p>
      
        <p>Learn more about the <a href="#create-account">benefits of creating an account</a>.</p>
    </div>
  </div>

  <div class="faq-item" id="search-history">
    <div class="faq-question" onclick="toggleFAQ('faq15')">
      <h3>Is my search history saved? Can I retrieve my searches later?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq15">
      <p>We don't track or save your search history, though we may offer an optional "recent searches" feature in the future.</p>
      <ul>
        <li><strong>No personal tracking:</strong> We collect aggregate search data but can't track back to you</li>
        <li><strong>Email alerts:</strong> Use bell button to set up notifications for your search</li>
        <li><strong>Save searches:</strong> After signing into your account, click the Bulk Actions menu → Add to Library. In the new library, note query in description</li>
        <li><strong>Revisit anytime:</strong> Access saved searches through your libraries</li>
      </ul>
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/libraries-scix">library management</a> and <a href="{{ site.baseurl }}/scixhelp/userpreferences-scix/myscix">email notifications</a>.</p>
    </div>
  </div>

  <div class="faq-item" id="export-citations">
    <div class="faq-question" onclick="toggleFAQ('faq14')">
      <h3>Can I export my search results to a citation manager like EndNote or Zotero?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq14">
      <p>Yes! Export your search results to citation managers:</p>
      <ul>
        <li><strong>Bulk Actions menu:</strong> Export search results in most scientific reference formats</li>
        <li><strong>Supported formats:</strong> EndNote, Zotero, BibTeX, RIS, AGU, and most other formats used in Earth and space sciences, physics, and mathematics</li>
        <li><strong>Libraries:</strong> Same export options available for saved libraries</li>
      </ul>
      <!-- <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/actions-scix/export">export options</a> and <a href="{{ site.baseurl }}/scixhelp/libraries-scix">library management</a>.</p> -->
    </div>
  </div>

  <div class="faq-item" id="targeted-search">
    <div class="faq-question" onclick="toggleFAQ('faq2')">
      <h3>How can I set up a highly targeted search on SciX?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq2">
      <p>Get precise results by being specific and combining details. Use field searches, operators, and filters:</p>
      <ul>
        <li><strong>Search text fields:</strong> <code>abs:</code>, <code>title:</code>, <code>full:</code>, <code>ack:</code></li>
        <li><strong>Search other fields:</strong> <code>author:</code>, <code>first_author:</code>, <code>year:</code>, <code>doctype:</code>, etc.</li>
        <li><strong>Combine fields: </strong> Use AND, OR, EXCLUDE (-), exact match (=) operators to combine different fields. If you enter more than one term, results must include all of them (i.e., default operator is AND).</li>
        <li><strong>Filter results:</strong> Use left panel filters after searching</li>
      </ul>
      
      <div class="search-examples-toggle" onclick="toggleSearchExamples()">
        <h4><i class="fa fa-search"></i> Search Examples <span class="examples-toggle">+</span></h4>
      </div>
      <div class="search-examples-content" id="search-examples">
        <div class="example-section">
          <h5>Author & Institution Searches:</h5>
          <ul>
            <li><code>author:"Manabe, Syukuro" year:1965-1970</code> → His early climate work</li>
            <li><code>first_author:"Haigh, Joanna" inst:"Imp Coll London"</code> → Her Imperial College papers</li>
          </ul>
        </div>
        <div class="example-section">
          <h5>Topic & Publication Searches:</h5>
          <ul>
            <li><code>abs:"volcano" full:"Fagradalsfjall" pubdate:[<"2021-02-01"]</code> → Pre-2021 volcano papers</li>
            <li><code>abs:"volcano" title:Krakatoa bibstem:"Natur"</code> → Nature volcano papers. See how to specify the <code>bibstem</code> for all journals <a href="https://www.scixplorer.org/journalsdb" target="_blank">here</a>.</li>
          </ul>
        </div>
        <div class="example-section">
          <h5>Combining with AND/OR:</h5>
          <ul>
            <li><code>author:("Manabe" OR "Wetherald") AND doctype:(inproceedings OR abstract)</code> → Conference papers by either</li>
            <li><code>author:"Lidmar-Bergström" title:("saprolite" OR "weathering")</code> → Her papers on either topic</li>
          </ul>
        </div>
        <div class="example-section">
          <h5>Excluding with Minus (-):</h5>
          <ul>
            <li><code>author:("Manabe" OR "Wetherald") -ack:NOAA</code> → Their papers without NOAA mentions</li>
            <li><code>author:"Cazenave" property:refereed -body:(precession OR nutation)</code> → Her refereed papers excluding Earth orientation</li>
          </ul>
        </div>
        <div class="example-section">
          <h5>Exact Match with Equals (=):</h5>
          <ul>
            <li><code>=author:"Makhubela, Tebogo V" abstract:"mine"</code> → Exact name match with "mine" in abstract</li>
            <li><code>author:"Makhubela, Tebogo V" =abstract:"mine" -abstract:"mining"</code> → Exact "mine" but not "mining"</li>
          </ul>
        </div>
      </div>
      
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/search-scix">advanced search techniques</a>.</p>
    </div>
  </div>
  
  <div class="faq-item" id="common-name-search">
    <div class="faq-question" onclick="toggleFAQ('faq3')">
      <h3>My colleague's name is not unique in my discipline. How can I search for their papers?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq3">
      <p>Common names like "Sun, Jin" (6.5K results) or "Smith, John" (13.2K results) can be tricky. Below are some strategies that can help.</p>
      <p>Example 1:</p>
      <ul>
        <li><strong>Be specific:</strong> <code>author:"Smith, J. S."</code> or <code>=author:"Smith, J"</code> → exact matches</li>
        <li><strong>Use ORCiD:</strong> <code>orcid:"0000-0001-6066-793X"</code> → guaranteed author match (click green ORCiD icon next to an author name to search by their ORCiD")</li>
      </ul>
      <p>Example 2:</p>
      <ul>
        <li><strong>Add topics:</strong> <code>author:"Sun, Jin"</code> AND <code>abs:"electromagnetic"</code> → filter by research area (6.5K results → ~150 results)</li>
        <li><strong>Author box filters:</strong> Click arrow next to author name → expand name variants → include/exclude specific variants or co-authors</li>
        <li><strong>Filter institutions (if known):</strong> Left panel → Institutions → Select "OR St U" or "ETH Zurich" (6.5K results → ~500). Find institution abbreviations <a href="https://github.com/adsabs/CanonicalAffiliations/blob/master/parent_child.tsv" target="_blank">here</a>.</li>
        <li><strong>Explore </strong>Menu → <strong>Author network:</strong> Select group of known collaborators → Add to filter and search. Results in the few papers of interest</li>
      </ul>
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/search-scix">advanced search techniques</a> and <a href="{{ site.baseurl }}/scixhelp/gettingstarted-scix/common-name">author search methods</a>.</p>
    </div>
  </div>
  
  <div class="faq-item" id="make-papers-discoverable">
    <div class="faq-question" onclick="toggleFAQ('faq4')">
      <h3>How can I make my papers more discoverable as an author with a common name?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq4">
      <p>Make your work easier to find:</p>
      <ul>
        <li><strong>Full name:</strong> Include middle initials for more specific matches</li>
        <li><strong>Stay consistent:</strong> Use same name format across all papers</li>
        <li><strong>Get ORCiD:</strong> <a href="https://orcid.org/">Create ID</a>, share on profiles, use on submissions, and <a href="{{ site.baseurl }}/scixhelp/orcid-scix">claim papers</a> in SciX</li>
        <li><strong>Name changes:</strong> <a href="{{ site.baseurl }}/scixhelp/policies-scix/name-changes/">See our name change policy</a> or <a href="mailto:help@scixplorer.org">email us</a> to link name variations</li>
        <li><strong>Share work:</strong> <a href="{{ site.baseurl }}/scixhelp/libraries-scix">Create public library</a> to showcase your papers</li>
      </ul>
    </div>
  </div>
  
  <div class="faq-item" id="find-collaborators">
    <div class="faq-question" onclick="toggleFAQ('faq5')">
      <h3>How can I use SciX to find collaborators for my research?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq5">
      <p>Search your topic (e.g., <code>abs:"sea level rise"</code> or <code>author:"Mitrovica, Jerry"</code>) then explore:</p>
      <ul>
        <li><strong>Explore Menu:</strong>
          <ul>
            <li><strong>Author networks:</strong> See who works together. Select individual authors or group of collaborators → Add to filter and search to see their papers.</li>
            <li><strong>Similar work:</strong> Search for your own papers and use the similar search to see related papers and authors. Learn more about <a href="{{ site.baseurl }}/scixhelp/search-scix/second-order/">similar search</a>.</li>
          </ul>
        </li>        
        <li><strong>Institution search:</strong> <code>inst:"Harvard U"</code> → find researchers at specific places</li>
        <li><strong>Funded projects:</strong> <code>abs:"sea level rise" doctype:proposal has:credit</code> → find published authors who were funded to work on this topic</li>
        <li><strong>Citations:</strong> Search for <code>citations(author:”Mitrovica, Jerry”)</code>. Click on the <strong>Explore</strong> menu to create a paper network or an author network of these citations</li>
      </ul>
      <p>Learn more in our <a href="{{ site.baseurl }}/scixhelp/gettingstarted-scix">Getting Started Tutorial</a>.</p>
    </div>
  </div>
  
  <div class="faq-item" id="track-citations">
    <div class="faq-question" onclick="toggleFAQ('faq6')">
      <h3>How can I track papers citing my work over time?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq6">
      <p>Track who's citing your work:</p>
      <ul>
        <li><strong>All citations:</strong> <code>citations(author:"Your Name")</code> → see papers citing your work</li>
        <li><strong>Specific papers:</strong> <code>citations(identifier:"PAPER_ID")</code> → track individual papers</li>
        <li><strong>Set alerts:</strong> Save searches by clicking the bell icon → get notified of new citations</li>
        <li><strong>View metrics:</strong> <strong>Metrics</strong> feature → see citation trends</li>
      </ul>
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/search-scix/citations-and-references">finding citations</a> and <a href="{{ site.baseurl }}/scixhelp/libraries-scix">library management</a>.</p>
    </div>
  </div>
  
  <div class="faq-item" id="exploration-features">
    <div class="faq-question" onclick="toggleFAQ('faq7')">
      <h3>What exploration and discovery features does SciX have?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq7">
      <p>Discover new research with these powerful tools:</p>
      <ul>
        <li>Use the <strong>Explore</strong> menu to access:
          <ul>
            <li><strong>Paper Network:</strong> See how papers connect through shared references</li>
            <li><strong>Author Networks:</strong> Visualize who collaborates with whom</li>
            <li><strong>Smart search tools:</strong> <code>similar()</code> → papers like yours, <code>trending()</code> → what's popular, <code>useful()</code> → methods & tools, <code>reviews()</code> → top papers that cite your search results. Learn more about these <a href="{{ site.baseurl }}/scixhelp/search-scix/second-order/">advanced search tools</a></li>
          </ul>
        </li>
        <li><strong>Co-reads:</strong> See what else people who read your paper also read</li>
        <li><strong>Highlights:</strong> Turn on using gear button above search results</li>
        <li><strong>Data & Software:</strong> <code>similar(PAPER_ID) doctype:software OR doctype:data</code> → find software or data relevant to a paper's topic</li>
      </ul>
    </div>
  </div>
    
  <div class="faq-item" id="what-is-library">
    <div class="faq-question" onclick="toggleFAQ('faq9')">
      <h3>What is a library and how is it useful?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq9">
      <p>Libraries help you organize and manage your research:</p>
      <ul>
        <li><strong>Group papers:</strong> Organize by topic, project, or any way you want</li>
        <li><strong>Build collections:</strong> Gather comprehensive lists for literature reviews</li>
        <li><strong>Share with others:</strong> Make public libraries or collaborate with colleagues</li>
        <li><strong>Export citations:</strong> Download in AGU, BibTeX, RIS, or other popular formats</li>
        <li><strong>Track impact:</strong> See citation patterns and metrics for your papers</li>
        <li><strong>Find connections:</strong> Use Paper Network to see how papers relate</li>
      </ul>
      <p>Learn how to <a href="{{ site.baseurl }}/scixhelp/libraries-scix/creating-libraries">create and manage libraries</a> (requires creating an account).</p>
    </div>
  </div>
  
  <div class="faq-item" id="request-corrections">
    <div class="faq-question" onclick="toggleFAQ('faq11')">
      <h3>My paper is not in SciX or some details are wrong. Can I request corrections?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq11">
      <p>Yes! Here's how to request corrections:</p>
      <ul>
        <li><strong>Missing papers:</strong> Use our <a href="https:/scixplorer.org/feedback/missingrecord">Submit Abstract Form</a> to report missing papers</li>
        <li><strong>Wrong details:</strong> Use the same form to report errors in existing records</li>
        <li><strong>Timing:</strong> New arXiv papers appear daily, published articles weekly</li>
        <li><strong>What we cover:</strong> Refereed articles, arXiv preprints, conference papers, and other scholarly works</li>
        <li><strong>Data sources:</strong> We work with publishers and arXiv for comprehensive coverage</li>
      </ul>
      <p>For other help, contact us at <a href="mailto:help@scixplorer.org">help@scixplorer.org</a>.</p>
    </div>
  </div>
    
  <div class="faq-item" id="why-use-scix">
    <div class="faq-question" onclick="toggleFAQ('faq13')">
      <h3>Why should I use SciX?</h3>
      <span class="faq-toggle">+</span>
    </div>
    <div class="faq-answer" id="faq13">
      <p>SciX makes research discovery and management easier:</p>
      <ul>
         <li><strong>Comprehensive coverage:</strong> Access millions of records — scientific papers, conference proceedings, PhD theses, data, software, proposals, and more — covering Earth and space sciences and related fields</li>
        <li><strong>Smart search:</strong> Find exactly what you need with powerful search tools and filters</li>
        <li><strong>Discover connections:</strong> See how papers, authors, and ideas connect through networks</li>
        <li><strong>Organize your work:</strong> Create libraries to manage and share your research</li>
        <li><strong>Track impact:</strong> Monitor citations and analyze the influence of your work</li>
        <li><strong>Stay current:</strong> Find trending papers to discover what's popular in your field</li>
        <li><strong>Free and open:</strong> Access all features without cost or restrictions</li>
        <li><strong>Built by scientists, for scientists:</strong> Designed specifically for the scientific community's needs</li>
      </ul>
      <p>Learn more about what SciX can do for you at <a href="https://www.scixplorer.org/home" target="_blank">scixplorer.org/home</a>.</p>
    </div>
  </div>
</div>

  </div>

  <!-- API Tab -->
  <div id="api" class="tab-content">
    <div class="tab-header">
      <h2>API Access</h2>
      <p>Use SciX programmatically with our comprehensive REST API.</p>
    </div>
    
    <!-- API Note -->
    <div class="api-note">
      <div class="api-note-content">
        <i class="fa fa-info-circle"></i>
        <strong>Note:</strong> SciX uses the same API as ADS (Astrophysics Data System, our sister website). If you're familiar with the ADS API, you can use the same endpoints and authentication methods with SciX.
      </div>
    </div>
    
    <div class="help-content">
      <div class="help-section">
        <h3><i class="fa fa-rocket"></i> First Steps</h3>
        <p>Get up and running with the SciX API in minutes:</p>
        <ul>
          <li><strong>Get your token:</strong> Visit your <a href="https://scixplorer.org/user/settings/token" target="_blank">API token settings</a></li>
          <li><strong>Read the docs:</strong> Check our <a href="https://github.com/adsabs/adsabs-dev-api/blob/master/README.md" target="_blank">introductory API documentation</a></li>
          <li><strong>Try examples:</strong> Explore our <a href="https://github.com/adsabs/adsabs-dev-api" target="_blank">Jupyter notebooks</a> with code samples</li>
        </ul>
      </div>
      
      <div class="help-section">
        <h3><i class="fa fa-book"></i> Full Documentation</h3>
        <p>Comprehensive API reference with interactive examples:</p>
        <ul>
          <li><strong>Interactive docs:</strong> <a href="https://ui.adsabs.harvard.edu/help/api/api-docs.html" target="_blank">Full API documentation</a> with live testing</li>
          <li><strong>Code examples:</strong> Python, R, and other language examples in our <a href="https://github.com/adsabs/adsabs-dev-api" target="_blank">GitHub repository</a></li>
          <li><strong>API terms:</strong> Read our <a href="{{ site.baseurl }}/scixhelp/terms-scix">API terms of use</a></li>
        </ul>
      </div>
      
      <div class="help-section">
        <h3><i class="fa fa-bolt"></i> Key Features</h3>
        <p>The SciX API provides access to:</p>
        <ul>
          <li><strong>Search:</strong> Query millions of scientific papers</li>
          <li><strong>Metrics:</strong> Access citation counts and impact data</li>
          <li><strong>Export:</strong> Download results in various formats (BibTeX, RIS, etc.)</li>
          <li><strong>Libraries:</strong> Manage and access your saved collections</li>
          <li><strong>Author data:</strong> Retrieve author information and networks</li>
        </ul>
      </div>
      
      <div class="help-section">
        <h3><i class="fa fa-cog"></i> Rate Limits & Support</h3>
        <p>API usage guidelines and support:</p>
        <ul>
          <li><strong>Rate limits:</strong> Free accounts have generous limits for most use cases</li>
          <li><strong>Higher limits:</strong> Contact us for increased rate limits if needed</li>
          <li><strong>Support:</strong> Email <a href="mailto:help@scixplorer.org">help@scixplorer.org</a> for API questions</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Resources Tab -->
  <div id="resources" class="tab-content">
    <div class="tab-header">
      <h2>Resources & Support</h2>
      <p>Find additional help, stay updated, and get the support you need.</p>
    </div>
    
    <!-- Help Navigation & Contact -->
    <div class="help-navigation-section">
      <div class="help-nav-content">
        <div class="help-nav-item">
          <h3><i class="fa fa-book"></i> Browse Topics</h3>
          <p>All help topics are organized in the left sidebar for easy navigation. Or simply use the search bar in the upper right to search the entire help site</p>
        </div>
        <div class="help-nav-item">
          <h3><i class="fa fa-newspaper-o"></i> Latest Updates</h3>
          <p>Visit the <a href="{{ site.baseurl }}/scixblog">SciX blog</a> for the latest information and updates</p>
        </div>
        <div class="help-nav-item">
          <h3><i class="fa fa-home"></i> Learn More About SciX</h3>
          <p>Discover all the features and capabilities of SciX at <a href="https://scixplorer.org/home" target="_blank">scixplorer.org/home</a></p>
        </div>
        <div class="help-nav-item">
          <h3><i class="fa fa-question-circle"></i> Need More Help?</h3>
          <p>Can't find what you're looking for? <a href="mailto:help@scixplorer.org">Contact us at help@scixplorer.org</a></p>
        </div>
      </div>
    </div>
  </div>

  <!-- Video Guide Tab -->
  <div id="video" class="tab-content">
    <div class="tab-header">
      <h2>Video Tutorial</h2>
      <p>Watch our comprehensive video guide to get started with SciX</p>
    </div>
    <div class="video-container-large">
<div class="scalable scalable-16-9">
  <div class="scalable-content">
    <iframe src="https://www.youtube.com/embed/LeTFmhmPjs0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  </div>
</div>
    </div>
  </div>

</div>


<style>
/* SciX Help Page Styles */

.help-page {
  /* Base styles for the help page */
}

.video-container-large {
  max-width: 900px;
  margin: 0 auto;
  background: #F2F2F2;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.scalable {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
}

.scalable-16-9 {
  padding-bottom: 56.25%;
}

.scalable-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.help-navigation-section {
  background: white;
  padding: 50px 20px;
  margin: 40px 0;
  border-top: 1px solid #e9ecef;
}

.help-nav-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
}

.help-nav-item {
  text-align: center;
  padding: 20px;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.help-nav-item:hover {
  background: #F2F2F2;
  transform: translateY(-2px);
}

.help-page .help-nav-item h3 {
  font-size: 1.4rem;
  color: #333;
  margin-bottom: 10px;
  font-weight: 600;
}

.help-nav-item p {
  color: #666;
  line-height: 1.5;
  margin: 0;
  font-size: 1.4rem;
}

.help-nav-item a {
  color: #049DD9;
  text-decoration: none;
  font-weight: 500;
}

.help-nav-item a:hover {
  color: #5FBFAE;
  text-decoration: underline;
}

/* API Note Styles */
.api-note {
  background: #f8f9fa;
  border-left: 4px solid #049DD9;
  border-radius: 4px;
  margin: 20px 0 30px 0;
  padding: 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.api-note-content {
  padding: 15px 20px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 1.4rem;
  line-height: 1.5;
  color: #333;
}

.api-note-content i {
  color: #049DD9;
  font-size: 1.4rem;
  margin-top: 2px;
  flex-shrink: 0;
}

.api-note-content strong {
  color: #049DD9;
  font-weight: 600;
}

/* Search Examples Styles */
.search-examples-toggle {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 15px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-examples-toggle:hover {
  background: #e9ecef;
  border-color: #049DD9;
}

.search-examples-toggle h4 {
  margin: 0;
  font-size: 1.4rem;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.search-examples-toggle i {
  color: #049DD9;
  margin-right: 8px;
}

.examples-toggle {
  font-size: 1.2rem;
  font-weight: bold;
  color: #049DD9;
}

.search-examples-content {
  display: none;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 20px;
  margin: -15px 0 15px 0;
}

.search-examples-content.active {
  display: block;
}

.example-section {
  margin-bottom: 20px;
}

.example-section:last-child {
  margin-bottom: 0;
}

.example-section h5 {
  color: #333;
  font-size: 1.3rem;
  margin-bottom: 10px;
  font-weight: 600;
}

.example-section ul {
  margin: 0;
  padding-left: 20px;
}

.example-section li {
  margin-bottom: 8px;
  font-size: 1.4rem;
  line-height: 1.5;
}


.tabbed-interface {
  max-width: 1200px;
  margin: 0 auto;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 40px;
}

.tab-navigation {
  display: flex;
  background: #F2F2F2;
  border-bottom: 1px solid #ddd;
  overflow-x: auto;
}

.tab-button {
  flex: 1;
  min-width: 150px;
  padding: 20px 15px;
  border: none;
  background: transparent;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 1.6rem;
  font-weight: 500;
  color: #666;
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;
}

.tab-button:hover {
  background: #e9ecef;
  color: #333;
}

.tab-button.active {
  background: white;
  color: #049DD9;
  border-bottom-color: #049DD9;
  font-weight: 600;
}

.tab-icon {
  font-size: 1.2rem;
}

.tab-content {
  display: none;
  padding: 20px 40px 40px 40px;
  min-height: 500px;
}

.tab-content.active {
  display: block;
}

.tab-header {
  text-align: center;
  margin-bottom: 15px;
}

.help-page .tab-header h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 15px;
  font-weight: 700;
}

.tab-header p {
  font-size: 2rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.help-content {
  max-width: 800px;
  margin: 0 auto;
}

.help-section {
  background: #F2F2F2;
  padding: 30px;
  margin-bottom: 20px;
  border-radius: 8px;
  border-left: 4px solid #049DD9;
}

.help-page .help-section h3 {
  color: #333;
  margin-bottom: 15px;
  font-size: 2rem;
}

.help-section p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
  font-size: 1.8rem;
}

.help-section ul {
  margin: 15px 0;
  padding-left: 20px;
}

.help-section li {
  color: #666;
  margin-bottom: 8px;
  line-height: 1.5;
  font-size: 1.8rem;
}

.help-section code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  color: #d63384;
}

.faq-toc {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin: 20px 0;
  border-left: 4px solid #049DD9;
}

.faq-toc h3 {
  margin: 0 0 15px 0;
  color: #333;
  font-size: 1.3rem;
  font-weight: 600;
}

.toc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
}

.toc-link {
  display: block;
  padding: 8px 12px;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.toc-link:hover {
  background: #049DD9;
  color: white;
  border-color: #049DD9;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.faq-container {
  max-width: 900px;
  margin: 30px auto;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.faq-item {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  overflow: hidden;
}

.faq-question {
  padding: 25px 30px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  transition: background-color 0.3s ease;
  border: none;
  width: 100%;
}

.faq-question:hover {
  background: #f8f9fa;
}

.help-page .faq-question h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #333;
  text-align: left;
  flex: 1;
}

.faq-toggle {
  font-size: 24px;
  font-weight: 900;
  color: #666;
  transition: all 0.3s ease;
  margin-left: 15px;
  min-width: 24px;
  text-align: center;
  display: inline-block;
  line-height: 1;
}

.faq-question.active .faq-toggle {
  color: #049DD9;
}

.faq-answer {
  padding: 0 30px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, padding 0.3s ease;
  background: #f8f9fa;
  border-top: 1px solid #eee;
}

.faq-answer.active {
  padding: 25px 30px;
  max-height: 1000px;
}

.faq-answer p {
  margin: 0 0 15px 0;
  color: #555;
  line-height: 1.6;
}

.faq-answer ul, .faq-answer ol {
  margin: 0 0 15px 0;
  padding-left: 25px;
  color: #555;
}

.faq-answer li {
  margin-bottom: 10px;
  line-height: 1.5;
}

.faq-answer a {
  color: #007bff;
  text-decoration: none;
}

.faq-answer a:hover {
  color: #0056b3;
  text-decoration: underline;
}

.faq-answer strong {
  color: #333;
  font-weight: 600;
}

/* Dark mode support */
[data-theme='dark'] .video-container-large {
  background: #404040;
}

[data-theme='dark'] .tabbed-interface {
  background: #2c2c2c;
}

[data-theme='dark'] .tab-navigation {
  background: #404040;
  border-bottom-color: #666;
}

[data-theme='dark'] .tab-button {
  color: #cccccc;
}

[data-theme='dark'] .tab-button:hover {
  background: #555;
  color: #ffffff;
}

[data-theme='dark'] .tab-button.active {
  background: #2c2c2c;
  color: #049DD9;
}

[data-theme='dark'] .help-page .tab-header h2 {
  color: #ffffff;
}

[data-theme='dark'] .tab-header p {
  color: #cccccc;
}

[data-theme='dark'] .help-section {
  background: #404040;
}

[data-theme='dark'] .help-page .help-section h3 {
  color: #ffffff;
}

[data-theme='dark'] .help-section p,
[data-theme='dark'] .help-section li {
  color: #cccccc;
}

[data-theme='dark'] .help-navigation-section {
  background: #2c2c2c;
  border-top-color: #404040;
}

[data-theme='dark'] .help-nav-item:hover {
  background: #404040;
}

[data-theme='dark'] .help-page .help-nav-item h3 {
  color: #ffffff;
}

[data-theme='dark'] .help-nav-item p {
  color: #cccccc;
}

[data-theme='dark'] .help-nav-item a {
  color: #049DD9;
}

[data-theme='dark'] .help-nav-item a:hover {
  color: #5FBFAE;
}

[data-theme='dark'] .faq-item {
  background: #2c2c2c;
  border: 1px solid #404040;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

[data-theme='dark'] .faq-question {
  background: #2c2c2c;
}

[data-theme='dark'] .faq-question:hover {
  background: #3a3a3a;
}

[data-theme='dark'] .help-page .faq-question h3 {
  color: #ffffff;
}

[data-theme='dark'] .faq-toggle {
  color: #cccccc;
}

[data-theme='dark'] .faq-question.active .faq-toggle {
  color: #049DD9;
}

[data-theme='dark'] .faq-answer {
  background: #1a1a1a;
  border-top: 1px solid #404040;
}

[data-theme='dark'] .faq-answer p {
  color: #e0e0e0;
}

[data-theme='dark'] .faq-answer ul, 
[data-theme='dark'] .faq-answer ol {
  color: #e0e0e0;
}

[data-theme='dark'] .faq-answer a {
  color: #4a9eff;
}

[data-theme='dark'] .faq-answer a:hover {
  color: #6bb6ff;
}

[data-theme='dark'] .faq-answer strong {
  color: #ffffff;
}

[data-theme='dark'] .faq-toc {
  background: #404040;
}

[data-theme='dark'] .faq-toc h3 {
  color: #ffffff;
}

[data-theme='dark'] .toc-link {
  background: #2c2c2c;
  border-color: #555;
  color: #cccccc;
}

[data-theme='dark'] .toc-link:hover {
  background: #049DD9;
  color: white;
  border-color: #049DD9;
}

/* Responsive design */
@media (max-width: 768px) {
  .tab-navigation {
    flex-direction: column;
  }
  
  .tab-button {
    min-width: auto;
    padding: 15px;
    border-bottom: 1px solid #ddd;
    border-right: none;
  }
  
  .tab-button.active {
    border-bottom-color: #ddd;
    border-right: 3px solid #049DD9;
  }
  
  .tab-content {
    padding: 15px 20px 20px 20px;
  }
  
  .help-page .tab-header h2 {
    font-size: 2.2rem;
  }
  
  .tab-header p {
    font-size: 1.2rem;
  }
}
</style>

<script>
function toggleFAQ(faqId) {
  const answer = document.getElementById(faqId);
  const question = answer.previousElementSibling;
  const toggle = question.querySelector('.faq-toggle');
  
  if (answer.classList.contains('active')) {
    answer.classList.remove('active');
    question.classList.remove('active');
    toggle.textContent = '+';
    // Save state to localStorage
    localStorage.setItem('faq_' + faqId, 'closed');
  } else {
    answer.classList.add('active');
    question.classList.add('active');
    toggle.textContent = '−';
    // Save state to localStorage
    localStorage.setItem('faq_' + faqId, 'open');
  }
}

function openTab(evt, tabName) {
  // Hide all tab contents
  const tabContents = document.getElementsByClassName('tab-content');
  for (let i = 0; i < tabContents.length; i++) {
    tabContents[i].classList.remove('active');
  }
  
  // Remove active class from all tab buttons
  const tabButtons = document.getElementsByClassName('tab-button');
  for (let i = 0; i < tabButtons.length; i++) {
    tabButtons[i].classList.remove('active');
  }
  
  // Show the selected tab content and mark button as active
  document.getElementById(tabName).classList.add('active');
  evt.currentTarget.classList.add('active');
  
  // Save the active tab to localStorage
  localStorage.setItem('scixhelp_active_tab', tabName);
}

// Toggle search examples
function toggleSearchExamples() {
  const content = document.getElementById('search-examples');
  const toggle = document.querySelector('.examples-toggle');
  
  // First ensure the parent FAQ is expanded
  const faqAnswer = content.closest('.faq-answer');
  const faqQuestion = faqAnswer.previousElementSibling;
  const faqToggle = faqQuestion.querySelector('.faq-toggle');
  
  if (!faqAnswer.classList.contains('active')) {
    faqAnswer.classList.add('active');
    faqQuestion.classList.add('active');
    faqToggle.textContent = '−';
  }
  
  if (content.classList.contains('active')) {
    content.classList.remove('active');
    toggle.textContent = '+';
  } else {
    content.classList.add('active');
    toggle.textContent = '−';
  }
}


// Smooth scrolling for anchor links and auto-open FAQ
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
      
      // If it's an FAQ item, open it automatically
      if (target.classList.contains('faq-item')) {
        const faqAnswer = target.querySelector('.faq-answer');
        const faqQuestion = target.querySelector('.faq-question');
        if (faqAnswer && faqQuestion) {
          // Close all other FAQs first
          document.querySelectorAll('.faq-answer.active').forEach(answer => {
            answer.classList.remove('active');
          });
          document.querySelectorAll('.faq-question.active').forEach(question => {
            question.classList.remove('active');
            const toggle = question.querySelector('.faq-toggle');
            if (toggle) toggle.textContent = '+';
          });
          
          // Open the target FAQ
          faqAnswer.classList.add('active');
          faqQuestion.classList.add('active');
          const toggle = faqQuestion.querySelector('.faq-toggle');
          if (toggle) toggle.textContent = '−';
        }
      }
    }
  });
});

// Restore FAQ states from localStorage
function restoreFAQStates() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const faqAnswer = item.querySelector('.faq-answer');
    const faqQuestion = item.querySelector('.faq-question');
    const faqId = faqAnswer.id;
    
    if (faqId) {
      const savedState = localStorage.getItem('faq_' + faqId);
      if (savedState === 'open') {
        faqAnswer.classList.add('active');
        faqQuestion.classList.add('active');
        const toggle = faqQuestion.querySelector('.faq-toggle');
        if (toggle) toggle.textContent = '−';
      }
    }
  });
}

// Restore tab state from localStorage
function restoreTabState() {
  const savedTab = localStorage.getItem('scixhelp_active_tab');
  if (savedTab) {
    // Find the tab button that corresponds to the saved tab
    const tabButtons = document.getElementsByClassName('tab-button');
    for (let i = 0; i < tabButtons.length; i++) {
      const button = tabButtons[i];
      const onclickAttr = button.getAttribute('onclick');
      if (onclickAttr && onclickAttr.includes(savedTab)) {
        // Simulate clicking the tab button
        openTab({ currentTarget: button }, savedTab);
        break;
      }
    }
  }
}

// Auto-open FAQ on page load if there's a hash in the URL
document.addEventListener('DOMContentLoaded', function() {
  // First restore saved FAQ states
  restoreFAQStates();
  
  // Restore the active tab
  restoreTabState();
  
  // Then handle URL hash if present
  if (window.location.hash) {
    const target = document.querySelector(window.location.hash);
    if (target && target.classList.contains('faq-item')) {
      const faqAnswer = target.querySelector('.faq-answer');
      const faqQuestion = target.querySelector('.faq-question');
      if (faqAnswer && faqQuestion) {
        // Close all other FAQs first
        document.querySelectorAll('.faq-answer.active').forEach(answer => {
          answer.classList.remove('active');
        });
        document.querySelectorAll('.faq-question.active').forEach(question => {
          question.classList.remove('active');
          const toggle = question.querySelector('.faq-toggle');
          if (toggle) toggle.textContent = '+';
        });
        
        // Open the target FAQ
        faqAnswer.classList.add('active');
        faqQuestion.classList.add('active');
        const toggle = faqQuestion.querySelector('.faq-toggle');
        if (toggle) toggle.textContent = '−';
      }
    }
  }
});
</script>
</div>
