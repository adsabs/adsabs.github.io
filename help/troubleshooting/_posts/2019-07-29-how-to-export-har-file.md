---
layout: post
title: "How to Generate a HAR File"
order: 2
---

### What is a HAR file?
HAR files are used to gather data from users' browser which can be used to troubleshoot network or resource issues with the ADS support staff.  This information includes detailed timing information about the requests made between the browser and the server.

### Google Chrome

1. Open __Google Chrome__
2. Navigate to [https://ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
3. Open the [ <i class="fa fa-ellipsis-v" aria-hidden="true"></i> ] menu > __More tools__ > __Developer Tools__
4. Select the __Network Tab__
5. Within the __Network Tab__, select the __Preserve Log__ option
6. Make sure that the circle in the top left is __RED__ ( <i class="fa fa-circle text-danger" aria-hidden="true"></i> ) 
 * This will begin recording requests
7. Reload the page
8. Once the page is done loading, go back to the __Dev Tools__, and click on the __Console Tab__
9. Right-click inside the console area and select __Save As__, save this file in a convenient place
10. Go back to the __Network Tab__, right-click on any network list entry and select __Save all as HAR with content__
11. Please upload both the __HAR__ file and the __Console Log__ file to the support thread

### Firefox

1. Open __Firefox__
2. Navigate to [https://ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
3. Open the [ <i class="fa fa-bars" aria-hidden="true"></i> ] menu > __Web Developer__ > __Network__
4. Select the __Network Tab__
5. Within the __Network Tab__, select the __Preserve Log__ option
7. Reload the page
8. Once the page is done loading, go back to the __Dev Tools__, and click on the __Console Tab__
9. Right-click inside the console area and click __Select All__ and __Copy Message__
10. Copy the messages to the support thread or save to a text file
10. Go back to the __Network Tab__, right-click on any network list entry and select __Save all as HAR__
11. Please upload both the __HAR__ file and the __Console Log__ file to the support thread

### Safari

1. Open __Safari__
2. Navigate to [https://ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu)
3. Open __Safari__ > __Preferences__ > __Advance__ > Click __Show Develop menu in menu bar__
4. Select __Develop__ in menu > __Show Web Inspector__ > select __Network Tab__
5. Within the __Network Tab__, select the __Preserve Log__ option
7. Reload the page
8. Once the page is done loading, go back to the __Dev Tools__
9. Click __Export__ at the top right of the __Network Tab__
10. Go to the __Console Tab__ and screenshot the messages
11. Please upload both the __HAR__ file and the __Console Log__ screenshot(s) to the support thread
