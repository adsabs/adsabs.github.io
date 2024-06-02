---
layout: post
title: "Technical Standards for Scanning Legacy Literature"
order: 6
---

NASA SciX contains extensive holdings of historic astronomy and astrophysics literature. As resources permit, we continue to digitize and ingest relevant items recommended by community members. In addition, we accept scans of appropriate material that meet these technical standards. Please contact the NASA SciX curators before beginning your project to ensure we can accommodate your proposal. We will also determine an effective delivery method then.   
  
We request that each page be scanned and saved as a single TIFF file. In all cases, a journal is scanned cover-to-cover with no pages skipped (even the blank ones). These images will need to comply with the following quality and naming requirements.  

## Quality requirements
  
Pages need to be scanned at a resolution of 600 dpi. Further requirements depend on the contents of the page. The following table specifies these requirements for each page type.  
  

| **Parameter** | **Setting** | 
| --- | --- |
| **Page type** | **Exclusively text and line art**|
| Dynamic range | 1-sample/pixel and 1-bit/sample |
| Compression |CCITT G4 encoding, with all image data encoded in a single strip |
| Photometric interpretation | min-is-white |
| Planar configuration | single image plane |
| Orientation | portrait |    
| **Page type** | **Page with gray-scale images** |
| Dynamic range | 1-sample/pixel and 8-bits/sample |
| Compression | LZW or Deflate |
| Photometric interpretation | min-is-black |
| Planar configuration | single image plane |
| Orientation | portrait |
| **Page type** | **Page with color images** |
| Dynamic range | 3-samples/pixel and 8-bits/sample |
| Compression | LZW or Deflate |
| Photometric interpretation | RGB |
| Planar configuration | single image plane |
| Orientation | portrait |

If a page contains both gray-scale and color content, follow the instructions for a page with color images.

Scanned images should have consistent borders around the text area and should be scanned in portrait orientation, with a maximum skewness of 2 degrees. Cropping of images is allowed, in order to clean up possible image contamination from paper borders. Resizing, however, is not allowed. The resolution of 600 dpi is to be maintained consistently. This means that the image dimensions divided by 600 should closely approximate the physical dimensions of the digitized area in inches.

## Page numbering
We expect you will take quality assurance measures to guarantee that pages will not be skipped during the scanning process, causing file names to be out of sync with the sequence of pages in the journal.  
  
We request that each page be scanned and saved as a single TIFF file, named after the journal acronym, volume and page number according to the templates described below; the journal acronym can be provided by the SciX team. If a journal acronym contains an ampersand (&), it needs to be replaced by a plus sign (+). Ideally, file extensions like .tif or .tiff should be omitted.

Typically, a page in a journal is one of the 6 following types: 

- **Regular pages:** these are the pages numbered with arabic numerals, which constitute the main body of the volume
- **Letter pages:** some journals have an introductory section of the journals where notes or letters to the editor are published
- **Inserts:** some journals contain inserts much larger than the regular page size, which are folded up and bound with the rest of the pages
- **Plates:** some journals have plates at the end of each volume or issue which are labeled by consecutive plate numbers
- **Front matter:** all pages preceding the "Regular" or “Letter” pages and starting from the cover
- **Back matter:** all pages following the last numbered page (or plate) and ending with the back cover

The file naming requirements for these page types are as follows:

| **Page type** | **Naming requirements** |
| --- | --- |
| Regular |The scans should be saved in files named JNLvvv.nnnn, where JNL is an abbreviation of the journal name, vvv is the volume number and nnnn is the zero-padded page number. For instance, page number 100 for volume 200 of the journal Astronomy & Astrophysics (A+A) should be saved in a TIFF file named A+A200.0100. Note: some journals may contain pages that, although not numbered, have an implied page number which can be easily inferred by their position within the sequence of numbered pages. In all cases these pages should be named after the corresponding implied page number. Sometimes regular pages are a combination of a letter and a number, like A1, in which case the letter should get included in the page numbering; for instance, the page "A10" in volume 33 of the journal "M+PS" should be saved in a file named "M+PS033.A010.". If a journal volume consists of multiple issues that all start on page 1, please contact us for more detailed instructions. |
| Letter | These pages are labeled with the letter "L" followed by an increasing number, starting from page L1. These scans should be saved in files named according to the following template: JNLvvv.Lnnn, where the file extension consists of the letter "L" followed by the zero-padded page number (three digits long). |
| Insert | If the physical size of the insert is 11" x 17" or smaller, a reduced copy of the scan should be created so that the resulting image size will match the typical page size of the journal being scanned. If the size of the insert is greater than 11" x 17", then multiple scans of the different parts of the image should be performed, each having a scanning area size equal to the one used for the typical pages of the current journal. If such inserts are not numbered according to the regular page numbering scheme, they should be assigned a file name created by appending a 3-digit sequential number to the filename of the preceding page. For instance, an insert appearing after page 100 of volume 200 of the journal Astronomy & Astrophysics should be saved in a file named A+A200.0100I001 |
| Plate | The plate scans should be saved in files named according to the following template: JNLvvv.nnnnPppp, where the file extension consists of the current page number nnnn (or the preceding page if the plate does not have a page number associated with it), followed letter "P" followed by the zero-padded plate number displayed on the page (ppp). |
| Front matter | All pages preceding the "Regular" or letter pages and starting from the cover should be scanned and saved in files JNLvvv.nnnnCddd, where the file extension consists of the number corresponding to the first numbered page following the cover pages (nnnn), followed by the letter "C," followed by a zero-padded sequence number (ddd). These pages are typically numbered using roman numerals and include all pages in the journal's "front matter" section. |
| Back matter | All pages following the last numbered page (or plate) and ending with the back cover should be scanned and saved in files named JNLvvv.nnnnZddd, where the file extension consists of the number corresponding to the last numbered page preceding the back-cover pages (nnnn), followed by the letter "Z," followed by a zero-padded sequence number (ddd) |

In case generating this file naming scheme presents problems, an alternative acceptable solution would be to provide us with a set of files and a lookup-table mapping the file names delivered into the file names in our requested format described above.
