---
layout: post_scix
title: 'SciX Help'
no-header: true
---

<div class="help-page">
<h2>Welcome to the SciX Help Pages</h2>

<p>Your comprehensive guide to discovering and managing scientific research. Get started in minutes with our quick start guide below, or use the search bar in the upper right to search the entire site.</p>

<!-- Hero Section
<div class="hero-section">
  <h3> What Can SciX Do? </h3>
  <div class="hero-features">
    <div class="hero-feature-card">
      <div class="hero-feature-icon">🔍</div>
      <h4>Powerful Search</h4>
      <p>Advanced syntax & filters</p>
    </div>
    <div class="hero-feature-card">
      <div class="hero-feature-icon">📚</div>
      <h4>Library Management</h4>
      <p>Organize & collaborate</p>
    </div>
    <div class="hero-feature-card">
      <div class="hero-feature-icon">📊</div>
      <h4>Analytics</h4>
      <p>Track citations & trends</p>
    </div>
    <div class="hero-feature-card">
      <div class="hero-feature-icon">⚡</div>
      <h4>API Access</h4>
      <p>Integrate workflows</p>
    </div>
    <div class="hero-feature-card">
      <div class="hero-feature-icon">🌐</div>
      <h4>Open & Free</h4>
      <p>No restrictions</p>
    </div>
    <div class="hero-feature-card">
      <div class="hero-feature-icon">👥</div>
      <h4>Community</h4>
      <p>Global researchers</p>
    </div>
  </div>
</div> -->

<!-- Tabbed Interface -->
<div class="tabbed-interface">
  <div class="tab-navigation">
    <button class="tab-button" onclick="openTab(event, 'what-does-scix')">
      <span class="tab-icon">🌟</span>
      What does SciX do?
    </button>
    <button class="tab-button active" onclick="openTab(event, 'quickstart')">
      <span class="tab-icon">🚀</span>
      Quick Start
    </button>
    <button class="tab-button" onclick="openTab(event, 'video')">
      <span class="tab-icon">🎥</span>
      Video Guide
    </button>
    <button class="tab-button" onclick="openTab(event, 'search')">
      <span class="tab-icon">🔍</span>
      Search Help
    </button>
    <button class="tab-button" onclick="openTab(event, 'libraries')">
      <span class="tab-icon">📚</span>
      Libraries
    </button>
    <button class="tab-button" onclick="openTab(event, 'api')">
      <span class="tab-icon">⚡</span>
      API
    </button>
    <button class="tab-button" onclick="openTab(event, 'troubleshooting')">
      <span class="tab-icon">🛠️</span>
      Troubleshooting
    </button>
  </div>

  <!-- What does SciX do? Tab -->
  <div id="what-does-scix" class="tab-content">
    <div class="tab-header">
      <h2>What does SciX do?</h2>
      <p>Discover the powerful features that make SciX the premier platform for scientific research discovery and management.</p>
    </div>

    <div class="hero-features">
      <div class="hero-feature-card">
        <div class="hero-feature-icon">🔍</div>
        <h4>Powerful Search</h4>
        <p>Advanced syntax & filters</p>
      </div>
      <div class="hero-feature-card">
        <div class="hero-feature-icon">📚</div>
        <h4>Library Management</h4>
        <p>Organize & collaborate</p>
      </div>
      <div class="hero-feature-card">
        <div class="hero-feature-icon">📊</div>
        <h4>Analytics</h4>
        <p>Track citations & trends</p>
      </div>
      <div class="hero-feature-card">
        <div class="hero-feature-icon">⚡</div>
        <h4>API Access</h4>
        <p>Integrate workflows</p>
      </div>
      <div class="hero-feature-card">
        <div class="hero-feature-icon">🌐</div>
        <h4>Open & Free</h4>
        <p>No restrictions</p>
      </div>
      <div class="hero-feature-card">
        <div class="hero-feature-icon">👥</div>
        <h4>Community</h4>
        <p>Global researchers</p>
      </div>
    </div>
  </div>

  <!-- Quick Start Tab (Default Active) -->
  <div id="quickstart" class="tab-content active">
    <div class="tab-header">
      <h2>Quick Start Guide</h2>
      <p>Get up and running with SciX in minutes. Click any question below to learn how to use our most popular features.</p>
    </div>

<div class="faq-container">
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq1')">
      <h3>How can I search for papers like any other search engine?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq1">
      <p>You can type any keyword, topic, author, or journal in the search bar, like in any other search platform. You can also drastically improve your search results by specifying the field you are searching for:</p>
      <ul>
        <li><strong>Basic search:</strong> Just type "exoplanets" or "Smith" and hit search</li>
        <li><strong>Targeted search:</strong> Use <code>author:"Smith, John"</code> or <code>year:2020</code> for precise results</li>
        <li><strong>Quick buttons:</strong> Click the field buttons above the search box for author, year, or abstract searches</li>
      </ul>
      <p>See our <a href="{{ site.baseurl }}/scixhelp/quickstart-scix">Quick Start Tutorial</a> for more tips.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq2')">
      <h3>How can I search for papers by an author with a common name?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq2">
      <p>Common names can be tricky, but these strategies help:</p>
      <ul>
        <li><strong>Be more specific:</strong> Use <code>author:"Smith, J. S."</code> instead of just <code>author:"Smith, J"</code></li>
        <li><strong>Add an equals sign:</strong> Use <code>=author:"Smith, J"</code> to find only exact matches</li>
        <li><strong>Use filters:</strong> Click on author names in the left panel to narrow results</li>
        <li><strong>Add more details:</strong> Include year, institution, or topic to narrow your search</li>
      </ul>
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/quickstart-scix">author search techniques</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq3')">
      <h3>How can I make my papers more discoverable as an author with a common name?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq3">
      <p>Make your work easier to find:</p>
      <ul>
        <li><strong>Use your full name:</strong> Include middle initials when publishing</li>
        <li><strong>Stay consistent:</strong> Use the same name format across all papers</li>
        <li><strong>Get an ORCID ID:</strong> Create an <a href="https://orcid.org/">ORCID ID</a> and <a href="{{ site.baseurl }}/scixhelp/orcid-scix">claim your papers</a> in SciX</li>
        <li><strong>Name changes:</strong> <a href="mailto:help@scixplorer.org">Email us</a> to link different name variations</li>
        <li><strong>Share your work:</strong> <a href="{{ site.baseurl }}/scixhelp/libraries">Create a public library</a> of your papers</li>
      </ul>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq4')">
      <h3>How can I set up a highly targeted search on SciX?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq4">
      <p>Get precise results by being specific:</p>
      <ul>
        <li><strong>Combine details:</strong> Use <code>author:"Smith, John" year:2020-2023</code> to find papers by Smith from 2020-2023</li>
        <li><strong>Use filters:</strong> Click filters in the left panel for journals, institutions, or topics</li>
        <li><strong>Example:</strong> <code>topic:"exoplanets" year:2020-2023</code> finds recent exoplanet papers</li>
        <li><strong>Search specific parts:</strong> Use <code>abs:</code> for abstracts, <code>title:</code> for titles</li>
        <li><strong>Combine with AND/OR:</strong> Mix terms to narrow or broaden your search</li>
      </ul>
      <p>See our <a href="{{ site.baseurl }}/scixhelp/search">search documentation</a> for more tips.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq5')">
      <h3>How can I use SciX to find collaborators for my research?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq5">
      <p>Find potential collaborators through SciX:</p>
      <ul>
        <li><strong>Author networks:</strong> Use the <strong>Explore</strong> menu to see who works together</li>
        <li><strong>Search by institution:</strong> Use <code>inst:"Harvard"</code> to find researchers at specific places</li>
        <li><strong>Look at co-authors:</strong> Check who frequently collaborates in your field</li>
        <li><strong>Find similar work:</strong> Use <code>similar(your_topic)</code> to find related papers and their authors</li>
        <li><strong>Citation connections:</strong> See whose work is cited together with yours</li>
      </ul>
      <p>Explore these features in our <a href="{{ site.baseurl }}/scixhelp/quickstart-scix">Quick Start Tutorial</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq6')">
      <h3>How can I track papers citing my work over time?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq6">
      <p>Keep track of who's citing your work:</p>
      <ul>
        <li><strong>Find all citations:</strong> Use <code>citations(author:"Your Name")</code> to see papers citing your work</li>
        <li><strong>Track specific papers:</strong> Use <code>citations(bibcode:YOUR_BIBCODE)</code> for individual papers</li>
        <li><strong>Set up alerts:</strong> Save searches to get notified of new citations</li>
        <li><strong>View metrics:</strong> Use the <strong>Metrics</strong> feature to see citation trends</li>
        <li><strong>Export data:</strong> Download citation data for analysis</li>
      </ul>
      <p>Learn more about <a href="{{ site.baseurl }}/scixhelp/search">citation tracking</a> and <a href="{{ site.baseurl }}/scixhelp/libraries">library management</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq7')">
      <h3>What exploration and discovery features does SciX have?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq7">
      <p>Discover new research with these powerful tools:</p>
      <ul>
        <li><strong>Paper Network:</strong> See how papers connect through shared references</li>
        <li><strong>Author Networks:</strong> Visualize who collaborates with whom</li>
        <li><strong>Smart search tools:</strong>
          <ul>
            <li><code>similar()</code> - Find papers like yours</li>
            <li><code>trending()</code> - See what's popular now</li>
            <li><code>useful()</code> - Find important methods and tools</li>
            <li><code>reviews()</code> - Locate comprehensive review papers</li>
          </ul>
        </li>
        <li><strong>Co-reads:</strong> See what else people who read your paper also read</li>
        <li><strong>Citation Helper:</strong> Find related papers through citation connections</li>
      </ul>
      <p>Access these features through the <strong>Explore</strong> menu on search results pages.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq8')">
      <h3>How can I filter search results effectively?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq8">
      <p>Narrow down your results with filters:</p>
      <ul>
        <li><strong>Authors:</strong> Include or exclude specific authors</li>
        <li><strong>Journals:</strong> Filter by publication or journal type</li>
        <li><strong>Years:</strong> Use sliders to pick date ranges</li>
        <li><strong>Institutions:</strong> Filter by research institutions</li>
        <li><strong>Topics:</strong> Filter by keywords, objects, or data availability</li>
        <li><strong>Collections:</strong> Limit to astronomy, physics, or general papers</li>
        <li><strong>Combine filters:</strong> Use AND, OR, and EXCLUDE when selecting multiple terms</li>
      </ul>
      <p>All filters are in the left panel of search results. Learn more about <a href="{{ site.baseurl }}/scixhelp/search">advanced filtering</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq9')">
      <h3>What is a library and how is it useful?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq9">
      <p>Libraries help you organize and manage your research:</p>
      <ul>
        <li><strong>Group papers:</strong> Organize by topic, project, or any way you want</li>
        <li><strong>Build collections:</strong> Create comprehensive lists for literature reviews</li>
        <li><strong>Share with others:</strong> Make public libraries or collaborate with colleagues</li>
        <li><strong>Export citations:</strong> Download in BibTeX, RIS, or other formats</li>
        <li><strong>Track impact:</strong> See citation patterns and metrics for your papers</li>
        <li><strong>Find connections:</strong> Use Paper Network to see how papers relate</li>
        <li><strong>Discover more:</strong> Use Citation Helper to find additional relevant papers</li>
      </ul>
      <p>Learn how to <a href="{{ site.baseurl }}/scixhelp/quickstart-scix">create and manage libraries</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq10')">
      <h3>How can I access SciX data programmatically?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq10">
      <p>Access SciX data through code:</p>
      <ul>
        <li><strong>Get your token:</strong> Visit your <a href="https://ui.adsabs.harvard.edu/user/settings/token">account settings</a> for an API token</li>
        <li><strong>Use the API:</strong> Access search, metrics, and export functions through code</li>
        <li><strong>See examples:</strong> Browse our <a href="https://github.com/adsabs/adsabs-dev-api">API notebooks</a> for code samples</li>
        <li><strong>Read docs:</strong> Check the <a href="https://github.com/adsabs/adsabs-dev-api/blob/master/README.md">API documentation</a></li>
        <li><strong>Try it live:</strong> Explore our <a href="{{ site.baseurl }}/scixhelp/api">interactive API docs</a> with live examples</li>
        <li><strong>Check limits:</strong> See the <a href="{{ site.baseurl }}/scixhelp/terms">API terms of use</a> for usage guidelines</li>
      </ul>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq11')">
      <h3>My paper is not in SciX or some details are wrong. Can I request corrections?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq11">
      <p>Yes! Here's how to request corrections:</p>
      <ul>
        <li><strong>Missing papers:</strong> Use our <a href="https://ui.adsabs.harvard.edu/feedback/correctabstract">Submit Abstract Form</a> to report missing papers</li>
        <li><strong>Wrong details:</strong> Use the same form to report errors in existing records</li>
        <li><strong>Timing:</strong> New arXiv papers appear daily, published articles weekly</li>
        <li><strong>What we cover:</strong> Refereed articles, arXiv preprints, conference papers, and other scholarly works</li>
        <li><strong>Data sources:</strong> We work with publishers and arXiv for comprehensive coverage</li>
      </ul>
      <p>For urgent corrections, contact us at <a href="mailto:help@scixplorer.org">help@scixplorer.org</a>.</p>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq12')">
      <h3>Where can I get more help?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq12">
      <p>We're here to help:</p>
      <ul>
        <li><strong>Help sections:</strong> Browse our comprehensive guides in the left navigation</li>
        <li><strong>Quick Start:</strong> Follow our <a href="{{ site.baseurl }}/scixhelp/quickstart-scix">step-by-step tutorials</a></li>
        <li><strong>Search tips:</strong> Learn advanced search techniques and syntax</li>
        <li><strong>Library guides:</strong> Discover how to organize and share your research</li>
        <li><strong>API help:</strong> Access code examples and interactive documentation</li>
        <li><strong>Contact us:</strong> Email us at <a href="mailto:help@scixplorer.org">help@scixplorer.org</a></li>
        <li><strong>Stay updated:</strong> Follow our <a href="{{ site.baseurl }}/scixblog">SciX blog</a> for news and tips</li>
      </ul>
    </div>
  </div>
  
  <div class="faq-item">
    <div class="faq-question" onclick="toggleFAQ('faq13')">
      <h3>Why should I use SciX?</h3>
      <span class="faq-toggle">▶</span>
    </div>
    <div class="faq-answer" id="faq13">
      <p>SciX makes research discovery and management easier:</p>
      <ul>
        <li><strong>Comprehensive coverage:</strong> Access millions of papers from astronomy, physics, and related fields</li>
        <li><strong>Smart search:</strong> Find exactly what you need with powerful search tools and filters</li>
        <li><strong>Discover connections:</strong> See how papers, authors, and ideas connect through networks</li>
        <li><strong>Organize your work:</strong> Create libraries to manage and share your research</li>
        <li><strong>Track impact:</strong> Monitor citations and analyze the influence of your work</li>
        <li><strong>Stay current:</strong> Find trending papers and discover what's popular in your field</li>
        <li><strong>Free and open:</strong> Access all features without cost or restrictions</li>
        <li><strong>Built for researchers:</strong> Designed specifically for the scientific community's needs</li>
      </ul>
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

  <!-- Search Help Tab -->
  <div id="search" class="tab-content">
    <div class="tab-header">
      <h2>Search Help</h2>
      <p>Master SciX's powerful search capabilities to find exactly what you need.</p>
    </div>
    <div class="help-content">
      <div class="help-section">
        <h3>Basic Search</h3>
        <p>Type any keyword, author name, or topic in the search box. SciX will search across titles, abstracts, and full text.</p>
      </div>
      <div class="help-section">
        <h3>Advanced Search Syntax</h3>
        <ul>
          <li><code>author:"Smith, John"</code> - Find papers by specific author</li>
          <li><code>year:2020</code> - Search within specific year</li>
          <li><code>abs:"exoplanets"</code> - Search in abstracts only</li>
          <li><code>full:"machine learning"</code> - Search in full text</li>
        </ul>
      </div>
      <div class="help-section">
        <h3>Search Operators</h3>
        <ul>
          <li><code>citations()</code> - Find papers citing a specific work</li>
          <li><code>similar()</code> - Find similar papers</li>
          <li><code>trending()</code> - Find popular papers</li>
          <li><code>reviews()</code> - Find review papers</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Libraries Tab -->
  <div id="libraries" class="tab-content">
    <div class="tab-header">
      <h2>Library Management</h2>
      <p>Organize your research with SciX libraries and collaborate with colleagues.</p>
    </div>
    <div class="help-content">
      <div class="help-section">
        <h3>Creating Libraries</h3>
        <p>Create personal or public libraries to organize your research papers by topic, project, or any other criteria.</p>
      </div>
      <div class="help-section">
        <h3>Sharing Libraries</h3>
        <p>Share your libraries with colleagues, students, or the broader community. Control who can view and edit your collections.</p>
      </div>
      <div class="help-section">
        <h3>Exporting Citations</h3>
        <p>Export your library contents in various formats including BibTeX, RIS, and plain text for use in other tools.</p>
      </div>
    </div>
  </div>

  <!-- API Tab -->
  <div id="api" class="tab-content">
    <div class="tab-header">
      <h2>API Access</h2>
      <p>Use SciX programmatically with our comprehensive REST API.</p>
    </div>
    <div class="help-content">
      <div class="help-section">
        <h3>Getting Started</h3>
        <p>Obtain an API token from your user preferences and start making requests to our REST API endpoints.</p>
      </div>
      <div class="help-section">
        <h3>Documentation</h3>
        <p>Comprehensive API documentation with examples in multiple programming languages.</p>
      </div>
      <div class="help-section">
        <h3>Rate Limits</h3>
        <p>Free accounts have generous rate limits. Contact us for higher limits if needed.</p>
      </div>
    </div>
  </div>

  <!-- Troubleshooting Tab -->
  <div id="troubleshooting" class="tab-content">
    <div class="tab-header">
      <h2>Troubleshooting</h2>
      <p>Common issues and solutions to help you get the most out of SciX</p>
    </div>
    <div class="help-content">
      <div class="help-section">
        <h3>Search Not Returning Results</h3>
        <ul>
          <li>Check your spelling and try broader search terms</li>
          <li>Remove filters that might be too restrictive</li>
          <li>Try searching in different fields (title, abstract, full text)</li>
          <li>Use quotation marks for exact phrases</li>
        </ul>
      </div>
      <div class="help-section">
        <h3>Library Issues</h3>
        <ul>
          <li>Ensure you're logged in to save papers to libraries</li>
          <li>Check if the library is set to private or public</li>
          <li>Try refreshing the page if papers don't appear</li>
          <li>Clear your browser cache if experiencing display issues</li>
        </ul>
      </div>
      <div class="help-section">
        <h3>API Problems</h3>
        <ul>
          <li>Verify your API token is correct and active</li>
          <li>Check if you've exceeded rate limits</li>
          <li>Ensure your request format matches the API documentation</li>
          <li>Contact support for higher rate limits if needed</li>
        </ul>
      </div>
      <div class="help-section">
        <h3>Still Need Help?</h3>
        <p>If you're still experiencing issues, please contact our support team with details about the problem you're encountering.</p>
      </div>
    </div>
  </div>
</div>

<!-- Why SciX Section -->
<div class="why-scix-section">
  <div class="section-header">
    <h2>Why Choose SciX?</h2>
    <p>Discover the features that make SciX the preferred research platform for scientists worldwide</p>
  </div>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon">🔍</div>
      <h3>Powerful Search</h3>
      <p>Find papers with advanced search syntax, filters, and smart suggestions</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📚</div>
      <h3>Library Management</h3>
      <p>Organize, share, and collaborate on research collections</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📊</div>
      <h3>Analytics & Insights</h3>
      <p>Track citations, discover trends, and analyze research impact</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">⚡</div>
      <h3>API Access</h3>
      <p>Integrate SciX into your workflow with our comprehensive API</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🌐</div>
      <h3>Open & Free</h3>
      <p>Always free to use with no restrictions or hidden costs</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">👥</div>
      <h3>Community</h3>
      <p>Join a global community of researchers and scientists</p>
    </div>
  </div>
</div>

<!-- Help Navigation & Contact -->
<div class="help-navigation-section">
  <div class="help-nav-content">
    <div class="help-nav-item">
      <h3>📚 Browse Topics</h3>
      <p>All help topics are organized in the left sidebar for easy navigation</p>
    </div>
    <div class="help-nav-item">
      <h3>🔍 Search Help</h3>
      <p>Use the search bar in the upper right to search the entire help site</p>
    </div>
    <div class="help-nav-item">
      <h3>📰 Latest Updates</h3>
      <p>Visit the <a href="{{ site.baseurl }}/scixblog">SciX blog</a> for the latest information and updates</p>
    </div>
    <div class="help-nav-item">
      <h3>💬 Need More Help?</h3>
      <p>Can't find what you're looking for? <a href="mailto:help@scixplorer.org">Contact us at help@scixplorer.org</a></p>
    </div>
  </div>
</div>

<style>
/* Hybrid Design: Option 3 Hero + Option 4 Tabs with Brand Colors */

.page-header {
  text-align: left;
  padding: 20px 20px 10px;
  max-width: 1200px;
  margin: 0 auto;
}


.hero-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px 20px 20px;
  background: transparent;
  border-radius: 12px;
  margin-bottom: 20px;
}

.help-page .hero-section h3 {
  font-size: 2rem;
  color: #333;
  margin: 0 0 20px 0;
  font-weight: 700;
  text-align: center;
}

.feature-pills {
  display: flex;
  gap: 15px;
  margin-bottom: 40px;
  flex-wrap: wrap;
}

.pill {
  background: white;
  border: 2px solid #049DD9;
  border-radius: 25px;
  padding: 8px 16px;
  font-size: 0.9rem;
  font-weight: 600;
  color: #049DD9;
  transition: all 0.3s ease;
}

.pill:hover {
  background: #049DD9;
  color: white;
  transform: translateY(-2px);
}

.pill-search {
  border-color: #049DD9;
  color: #049DD9;
}

.pill-libraries {
  border-color: #5FBFAE;
  color: #5FBFAE;
}

.pill-api {
  border-color: #97BF41;
  color: #97BF41;
}

.pill-analytics {
  border-color: #BFAC4B;
  color: #BFAC4B;
}

.hero-features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 0;
}

.hero-feature-card {
  background: white;
  border: 2px solid #049DD9;
  border-radius: 8px;
  padding: 12px 8px;
  text-align: center;
  transition: all 0.3s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.hero-feature-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  border-color: #5FBFAE;
}

.hero-feature-icon {
  font-size: 1.5rem;
  margin-bottom: 6px;
}

.help-page .hero-feature-card h4 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
  line-height: 1.2;
}

.hero-feature-card p {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
  line-height: 1.3;
}

.video-container-large {
  max-width: 900px;
  margin: 0 auto;
  background: #F2F2F2;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.why-scix-section {
  background: #F2F2F2;
  padding: 60px 20px;
  margin: 40px 0;
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
  font-size: 1.2rem;
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

.section-header {
  text-align: center;
  margin-bottom: 50px;
}

.help-page .section-header h2 {
  font-size: 2.2rem;
  color: #333;
  margin-bottom: 15px;
  font-weight: 700;
}

.section-header p {
  font-size: 1.2rem;
  color: #666;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
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
  font-size: 1rem;
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

/* Hero Features within Tabs */
.hero-features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 25px;
  margin-top: 30px;
}

.hero-feature-card {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border: 2px solid #e9ecef;
  border-radius: 15px;
  padding: 30px 25px;
  text-align: center;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.hero-feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(4, 157, 217, 0.1), transparent);
  transition: left 0.6s ease;
}

.hero-feature-card:hover::before {
  left: 100%;
}

.hero-feature-card:hover {
  transform: translateY(-8px);
  border-color: #049DD9;
  box-shadow: 0 15px 30px rgba(4, 157, 217, 0.2);
}

.hero-feature-icon {
  font-size: 3rem;
  margin-bottom: 20px;
  display: block;
  animation: iconFloat 3s ease-in-out infinite;
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

.hero-feature-card h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 12px;
  position: relative;
  z-index: 2;
}

.hero-feature-card p {
  font-size: 1rem;
  color: #666;
  margin: 0;
  position: relative;
  z-index: 2;
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
  font-size: 1.5rem;
}

.help-section p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 10px;
  font-size: 1.2rem;
}

.help-section ul {
  margin: 15px 0;
  padding-left: 20px;
}

.help-section li {
  color: #666;
  margin-bottom: 8px;
  line-height: 1.5;
  font-size: 1.2rem;
}

.help-section code {
  background: #e9ecef;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  color: #d63384;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
}

.feature-card {
  background: #F2F2F2;
  padding: 30px;
  border-radius: 12px;
  text-align: center;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.feature-card:hover {
  background: white;
  border-color: #049DD9;
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.help-page .feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: #333;
  font-weight: 600;
}

.feature-card p {
  color: #666;
  line-height: 1.5;
  margin: 0;
  font-size: 1.2rem;
}

/* Dark mode support */
[data-theme='dark'] .help-page .hero-section {
  background: transparent !important;
}

[data-theme='dark'] .help-page .page-header h1 {
  color: #ffffff;
}

[data-theme='dark'] .page-subtitle {
  color: #cccccc;
}

[data-theme='dark'] .help-page .hero-section h3 {
  color: #ffffff;
}

[data-theme='dark'] .pill {
  background: #404040;
  color: #049DD9;
}

[data-theme='dark'] .hero-feature-card {
  background: #404040;
  border-color: #049DD9;
}

[data-theme='dark'] .hero-feature-card:hover {
  border-color: #5FBFAE;
}

[data-theme='dark'] .help-page .hero-feature-card h4 {
  color: #ffffff;
}

[data-theme='dark'] .hero-feature-card p {
  color: #cccccc;
}

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

[data-theme='dark'] .hero-feature-card {
  background: linear-gradient(135deg, #2c2c2c 0%, #404040 100%);
  border-color: #404040;
}

[data-theme='dark'] .hero-feature-card:hover {
  border-color: #049DD9;
  box-shadow: 0 15px 30px rgba(4, 157, 217, 0.3);
}

[data-theme='dark'] .hero-feature-card h4 {
  color: #ffffff;
}

[data-theme='dark'] .hero-feature-card p {
  color: #cccccc;
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

[data-theme='dark'] .feature-card {
  background: #404040;
}

[data-theme='dark'] .feature-card:hover {
  background: #2c2c2c;
}

[data-theme='dark'] .help-page .feature-card h3 {
  color: #ffffff;
}

[data-theme='dark'] .feature-card p {
  color: #cccccc;
}

[data-theme='dark'] .why-scix-section {
  background: #2c2c2c;
}

[data-theme='dark'] .help-page .section-header h2 {
  color: #ffffff;
}

[data-theme='dark'] .section-header p {
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

/* Responsive design */
@media (max-width: 768px) {
  
  .hero-section {
    padding: 15px;
    text-align: center;
  }
  
  .hero-features {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .hero-feature-card {
    padding: 12px 8px;
  }
  
  .hero-feature-icon {
    font-size: 1.3rem;
  }
  
  .help-page .hero-section h3 {
    font-size: 1.8rem;
  }
  
  .help-page .hero-feature-card h4 {
    font-size: 1.1rem;
  }
  
  .hero-feature-card p {
    font-size: 1rem;
  }
  
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
  
  .features-grid {
    grid-template-columns: 1fr;
  }
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
  font-size: 20px;
  font-weight: bold;
  color: #666;
  transition: transform 0.3s ease;
  margin-left: 15px;
  min-width: 20px;
  text-align: center;
}

.faq-question.active .faq-toggle {
  transform: rotate(90deg);
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

/* Dark mode styles */
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
</style>

<script>
function toggleFAQ(faqId) {
  const answer = document.getElementById(faqId);
  const question = answer.previousElementSibling;
  const toggle = question.querySelector('.faq-toggle');
  
  if (answer.classList.contains('active')) {
    answer.classList.remove('active');
    question.classList.remove('active');
    toggle.textContent = '▶';
  } else {
    answer.classList.add('active');
    question.classList.add('active');
    toggle.textContent = '▼';
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
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});
</script>
</div>
