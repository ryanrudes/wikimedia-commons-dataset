# Wikimedia Commons Image Dataset

<ins>A highly organized and potentially very large image dataset for ML.</ins>

Wikimedia Commons is an online repository of openly-available media files, such as image, audio, video, and JSON files. You may view the current quantity of available content [here](https://commons.wikimedia.org/wiki/Special:MediaStatistics).

As of June 24, 2020, the database consists of approximately 56.47 million files of image content of file format .jpg, .jpeg, or .png.

The size of the dataset provides vast potential for use in machine learning. Another benefit is the detailed categorization of the contents of this media collection, allowing for rather simple data extraction for supervised learning methods. In summary, the benefits of this dataset are fantastic organization of classes, wide variety of features, and a large number of images.

There does, indeed, exist an API for data scraping Wikipedia Commons, however, it introduces an unsatisfying limit of 500 files at a time.

This Python script, however, recursively iterates over all categories and subcategories of the Wikipedia Commons image dataset, extracting all valid images, and saving them approperiately in identically organized folders.

I suggest using the free GPU provided by [paperspace.com](https://www.paperspace.com), which on the most recent version (v1.6), which uses multithreading, acheives between 70-100 images per second. Prior versions are slower and prone to bugs, so I do not suggest using older versions.

Setup is fairly simple:
1.  cd to the approperiate directory, then install the required packages (if they are not installed already on your machine) with: ```pip3 install -r requirements.txt```
2.  Next, create an empty folder, titled "Images", inside of the directory.
3.  Finally, of course, you must run this command to begin data scraping ```python3 scrape_wikimedia_v1.2.py``` (or the approperiate filename corresponding to the most recent version).

When the program begins (note that if you are running v1.0, it will not print anything to the console), you will notice subdirectories beginning to appear within the "Images" folder. In addition, a text file, titled "Sitemap.txt" will appear in the directory, which will contain the categories, with each additional subcategory indented approperiately. Over time, these subdirectories will become filled with images corresponding to the description provided by each particular folder's name. This organization of image content is identical to that of the Wikimedia Commons collection, which you can view [here](https://commons.wikimedia.org/wiki/Category:Categories).

# Version History
- __v1.0__: Initial data scraper. <br/>
  * Issues:
    1.  Rare improper parsing of image directories, resulting in issues pertaining to directories not being found.
    2.  Category parser does not pick up on items following a gray arrow symbol on the Wikimedia Commons website.
    3.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.
    4.  Console produces a large amount of text when run in the Mac terminal. Must add line to clear this status output before each time a new one is printed.
    
- __v1.1__ <br/>
  * Updates since v1.0:
    1.  Increased speed of data scraper
    2.  Added line to clear the console each time a new status update was printed.
    3.  Fixed issue #2 from v1.0
  * Issues:
    1.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.
    2.  Rare improper parsing of image directories, resulting in issues pertaining to directories not being found.
    3.  The improper parsing of categories from a Wikimedia Commons page results in undesired stopping of the data scraper program, which encounters an error upon this occurance.
    4.  When save directory contains the forward slash character, a confusion occurs, because the program interprets the "/" as a different subdirectory than the one actually desired.
 
- __v1.2__ <br/>
  * Updates since v1.1:
    1.  Fixed issue #2 from v1.1
  * Issues:
    1.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.
    2.  The improper parsing of categories from a Wikimedia Commons page results in undesired stopping of the data scraper program, which encounters an error upon this occurance.
    3.  When save directory contains the forward slash character, a confusion occurs, because the program interprets the "/" as a different subdirectory than the one actually desired.

- __v1.3__: <br/>
  * Updates since v1.2:
    1.  Fixed issue #2 from v1.2
  * Issues:
    1.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.
    2.  When save directory contains the forward slash character, a confusion occurs, because the program interprets the "/" as a different subdirectory than the one actually desired.
    
- __v1.4__: <br/>
  * Updates since v1.3:
    1.  Fixed issue #2 from v1.3
  * Issues:
    1.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.

- __v1.5__: <br/>
  * Updates since v1.4:
    1.  There were still some remnants of the problem nearly solved in v1.4. This issue is now fully eradicated.
  * Issues:
    1.  Parser does not search for categories listed on split pages. If a page on Wikimedia Commons lists a large number of categories, it is often split into two or more pages. The parser is not designed to search for these yet.

- __v1.6__: <br/>
  * Updates since v1.5:
    1.  Fixed issue #1 from v1.5
    2.  Implemented multithreading, which increased the average rate of the data scraper by approx. 3-4x
  * Issues: No known bugs have been found in this version thus far.
