---
layout: post
title: "Problems Exporting to ADS Classic"
order: 1
---

If nothing happens when you try to export records to ADS Classic, it is possible that you may be blocking popups.  The issue has to do with browsers restricting the way we communicate with ADS Classic.


### Chrome

1. Open up a new window/tab and navigate to [chrome://settings/content/popups](chrome://settings/content/popups).

2. Click on the **ADD** button under *Allow* section.
   
   ![chrome-popup-settings](/img/chrome-popup-settings.png){:width="800px"}


3. Type or copy/paste **[.*]adsabs.harvard.edu** into the input box.

   ![chrome-popup-add-site-1](/img/popup-settings-chrome-add-site-1.png){:width="800px"}


4. Click on **ADD** to include ADS Beta to the list of allowed sites.

   ![popup-settings-chrome-add-site](/img/popup-settings-chrome-add-site.png){:width="800px"}


5. **Reload** the ADS Beta page to refresh the site settings.

---

### Firefox

1. Open up a new window/tab and navigate to [about:preferences#privacy](about:preferences#privacy).

2. Scroll down to the **Permission** Section.

3. Find **Block Popups** and click on **Exceptions**.

   ![preference-section-firefox](/img/preferences-section-firefox-arrow.png){:width="800px"}

4. In the dialog that popups, type in **https://ui.adsabs.harvard.edu** and click **Allow**.

   ![firefox-add-site-2](/img/firefox-add-site-2.png){:width="800px"}

   ![firefox-add-site-3](/img/firefox-add-site-3.png){:width="800px"}

5. Click on **Save Changes**.

6. **Reload** ADS Beta, and you should be able to export to ADS Classic.

*Note: Firefox may still warn about connecting over an insecure connection when exporting*