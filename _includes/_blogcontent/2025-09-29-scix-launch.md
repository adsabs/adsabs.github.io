It's official - [SciX](http://scixplorer.org) is here! After months of development, testing, and feedback from our brilliant community, we're thrilled to launch Science Explorer, or SciX to its friends, out into the world.

> **So, what is SciX?** Think of it as your one-stop platform for exploring research across *Earth, environmental and space sciences, including planetary science, heliophysics, geology, geophysics, atmospheric sciences and oceanography*.

From tracking solar storms, to uncovering the secrets of distant planets, to understanding the changing dynamics of our own Earth, SciX is designed to be your research co-pilot. [Watch our launch video here](https://www.youtube.com/watch?v=sgJ-LolRLu8), and learn more about [what SciX can do here](https://www.scixplorer.org/home).

We've built SciX as a natural evolution of the [Astrophysics Data System (ADS)](https://ui.adsabs.harvard.edu), bringing its powerful capabilities into new domains. For ADS users, SciX uses your familiar search queries and workflows to access an even more comprehensive collection of curated scientific literature, software, and data. <mark>Transitioning from ADS to SciX is seamless</mark>: existing user accounts, personal libraries, and notifications created via ADS are available and accessible through SciX. No ADS links or services become obsolete with the introduction of this interdisciplinary portal, but SciX users benefit from the newest features we have developed for it.

<div style="height: 10px;"></div>
<div class="highlight-box highlight-box-teal">
With expanded coverage, intuitive search, smart recommendations, and tools for collaboration, SciX makes research more <strong>discoverable, connected, and accessible</strong> than ever before.
</div>
<div style="height: 15px;"></div>


**Why does this matter?** Because the big questions - about our planet, our local star, and our universe beyond - don't fit neatly into one discipline. They require all of us, across communities, to work together. SciX helps break down research silos, making it easier for researchers in heliophysics to connect with Earth scientists, or for planetary scientists to explore insights from astrophysics. 

> **Because you don't know what you don't know.** SciX helps uncover those underexplored but interrelated areas of research that might enable the breakthrough you've been looking for.

SciX is a project created by the ADS team and operated out of the Smithsonian Astrophysical Observatory under a NASA Cooperative Agreement. SciX builds on decades of open research infrastructure and collaboration that's powered discoveries big and small. <mark>It's a platform created and developed by scientists, for scientists</mark> - and we can't wait to see how you'll use it.

<div style="height: 15px;"></div>
<div class="highlight-box highlight-box-yellow">
<strong>This is just the beginning.</strong> The launch is a milestone, but the real journey is what comes next - and that will be shaped by you, our community. So explore, share, and <a href="https://docs.google.com/forms/d/e/1FAIpQLSdm9JYp8fFm1UwtR4Nman_s60FTGnDitW7dcsBZoYcrsdLQig/viewform?usp=header">let us know how SciX helps spark your research adventures</a>.
</div>

## Welcome aboard!

<div class="text-center">
    <img class="img-thumbnail" src="{{ site.baseurl }}/blog/images/scixlaunch2025.png" />
</div>
<br>

---

<!-- ## Press Coverage -->

<div class="press-coverage-container">
  <div class="press-coverage-tab" onclick="togglePressCoverage()">
    <span class="tab-text">Press Coverage</span>
  </div>
  
  <div id="press-coverage-box" class="press-coverage-box" onclick="togglePressCoverage()">
    <div class="press-coverage-header">
      <h4><i class="fa fa-newspaper-o"></i>Press Coverage</h4>
      <button class="close-button" onclick="event.stopPropagation(); togglePressCoverage();">&times;</button>
    </div>
    <ul>
      <li><a href="https://www.cfa.harvard.edu/news/new-nasa-backed-research-platform-scix-expands-open-science" target="_blank">New NASA-Backed Research Platform SciX Expands Open Science</a><br><small>Center for Astrophysics | Harvard & Smithsonian</small></li>
      <li><a href="https://science.data.nasa.gov/features-events/scix-launch" target="_blank">SciX: A New Era for NASA Research Discovery</a><br><small>NASA Science Data Portal</small></li>
    </ul>
  </div>
</div>

<!-- Desktop version -->
<div id="press-coverage-box-desktop" class="press-coverage-box-desktop">
  <h4 style="margin-top: 0; color: #495057; font-size: 16px;"><i class="fa fa-newspaper-o" style="margin-right: 8px;"></i>Press Coverage</h4>
  <ul style="margin-bottom: 0; padding-left: 20px;">
    <li style="margin-bottom: 8px;"><a href="https://www.cfa.harvard.edu/news/new-nasa-backed-research-platform-scix-expands-open-science" target="_blank" style="color: #007bff; text-decoration: none;">New NASA-Backed Research Platform SciX Expands Open Science</a><br><small style="color: #6c757d;">Center for Astrophysics | Harvard & Smithsonian</small></li>
    <li><a href="https://science.data.nasa.gov/features-events/scix-launch" target="_blank" style="color: #007bff; text-decoration: none;">SciX: A New Era for NASA Research Discovery</a><br><small style="color: #6c757d;">NASA Science Data Portal</small></li>
  </ul>
</div>

<style>
  .press-coverage-container {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 1000;
    display: none;
  }
  
  .press-coverage-tab {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    color: #049DD9;
    padding: 15px 8px;
    border-radius: 8px 0 0 8px;
    cursor: pointer;
    box-shadow: -2px 0 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    min-height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(4, 157, 217, 0.2);
  }
  
  .press-coverage-tab:hover {
    background: rgba(4, 157, 217, 0.1);
    transform: translateX(-5px);
    box-shadow: -4px 0 12px rgba(0,0,0,0.15);
    border-color: rgba(4, 157, 217, 0.4);
  }
  
  .tab-text {
    font-weight: 300;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  
  .press-coverage-box {
    position: absolute;
    top: 0;
    right: 0;
    width: 280px;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 20px;
    font-size: 14px;
    z-index: 1000;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transform: translateX(100%);
    transition: transform 0.3s ease;
    overflow: hidden;
  }
  
  .press-coverage-box.show {
    transform: translateX(0);
  }
  
  .press-coverage-header {
    background: none;
    color: #495057;
    padding: 0;
    display: block;
    margin-bottom: 15px;
  }
  
  .press-coverage-header h4 {
    margin: 0;
    font-size: 16px;
    font-weight: 600;
    color: #495057;
  }
  
  .press-coverage-header i {
    margin-right: 8px;
  }
  
  .close-button {
    background: none;
    border: none;
    color: #495057;
    font-size: 20px;
    cursor: pointer;
    padding: 0;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: background-color 0.2s ease;
    position: absolute;
    top: 10px;
    right: 10px;
  }
  
  .close-button:hover {
    background-color: rgba(0,0,0,0.1);
  }
  
  .press-coverage-box ul {
    margin: 0;
    padding-left: 20px;
    list-style: none;
  }
  
  .press-coverage-box li {
    margin-bottom: 8px;
  }
  
  .press-coverage-box li:last-child {
    margin-bottom: 0;
  }
  
  .press-coverage-box a {
    color: #007bff;
    text-decoration: none;
    line-height: 1.4;
    display: block;
    margin-bottom: 5px;
  }
  
  .press-coverage-box a:hover {
    color: #0056b3;
    text-decoration: underline;
  }
  
  .press-coverage-box small {
    color: #6c757d;
    font-size: 12px;
  }
  
  @media (max-width: 768px) {
    .press-coverage-container {
      display: block;
    }
    
    .press-coverage-box {
      width: 280px;
    }
  }
  
  .press-coverage-box-desktop {
    position: absolute;
    top: 250px;
    right: -275px;
    width: 280px;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 20px;
    font-size: 14px;
    z-index: 1000;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
  }
  
  .press-coverage-box-desktop.hidden {
    transform: translateX(100%);
  }
  
  @media (max-width: 768px) {
    .press-coverage-box-desktop {
      display: none;
    }
  }
  
  @media (min-width: 769px) {
    .press-coverage-container {
      display: none;
    }
  }
</style>

<script>
function togglePressCoverage() {
  const box = document.getElementById('press-coverage-box');
  box.classList.toggle('show');
}
</script>
