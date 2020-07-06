# Wikimedia Commons Image Dataset

<ins>A highly organized and potentially very large image dataset for ML.</ins>

Wikimedia Commons is an online repository of openly-available media files, such as image, audio, video, and JSON files. You may view the current quantity of available content [here](https://commons.wikimedia.org/wiki/Special:MediaStatistics).

As of June 24, 2020, the database consists of approximately 56.47 million files of image content of file format .jpg, .jpeg, or .png.

The size of the dataset provides vast potential for use in machine learning. Another benefit is the detailed categorization of the contents of this media collection, allowing for rather simple data extraction for supervised learning methods. In summary, the benefits of this dataset are fantastic organization of classes, wide variety of features, and a large number of images.

There does, indeed, exist an API for data scraping Wikipedia Commons, however, it introduces an unsatisfying limit of 500 files at a time.

This Python script, however, recursively iterates over all categories and subcategories of the Wikipedia Commons image dataset, extracting all valid images, and saving them approperiately in identically organized folders.

The speed of content extracting matches, and likely surpasses the rate of the official Wikipedia Commons Python API, thus providing benefits towards computational time required. On a Google Colab high-RAM runtime, it averages 14-17 images, downloaded, labeled, and categorized approperiately, each second.

However, I suggest using the free GPU provided by [paperspace.com](https://www.paperspace.com), which acheived the most satisfactory speed of 33-75 images per second.

Although this method of extraction and download is faster, the dataset is still <b>vast</b>, and therefore, the process is certainly <b>not</b> rapid.

Once the dataset is fully completed, I will compress it into a zip file, and add it to this repo. In the meanwhile, feel free to do some datascraping yourself, or, if you'd like to contribute computational resources, see below*.

I highly recommend always using the most recent version of the data scraper; it will not require any additional installations.

Setup is fairly simple:
1.  cd to the approperiate directory, then install the required packages (if they are not installed already on your machine) with: ```pip3 install -r requirements.txt```
2.  Next, create an empty folder, titled "Images", inside of the directory.
3.  Finally, of course, you must run this command to begin data scraping ```python3 scrape_wikimedia_v1.2.py``` (or the approperiate filename corresponding to the most recent version).

When the program begins (note that if you are running v1.0, it will not print anything to the console), you will notice subdirectories beginning to appear within the "Images" folder. In addition, a text file, titled "Sitemap.txt" will appear in the directory, which will contain the categories, with each additional subcategory indented approperiately. Over time, these subdirectories will become filled with images corresponding to the description provided by each particular folder's name. This organization of image content is identical to that of the Wikimedia Commons collection, which you can view [here](https://commons.wikimedia.org/wiki/Category:Categories).

*If you would like to contribute computational resources to this effort, simply message me at my preferred email address (ryanrudes@gmail.com), which is listed on my Github profile with a message in the following format:

> ### I Would Like To Contribute Computational Resources To This Dataset
> Hi, my name is __________ (this may be anonymous, if you'd like). <br/>
> My personal computer runs on __________ _GB_ of RAM. <br/>
> It uses the __________ operating system. <br/>
> I have tried to, and found that I can successfully run the most recent version of the data scraper on my computer/preferred location (ie. programming notebook). <br/>
> I am capable of providing a **maximum** of __________ _hours_ of computational time on my computer to this dataset. <br/>
> I can designate a **maximum** of __________ _gigabytes_ of disk memory to temporarily store the scraped images until they are added to the dataset, at which point, I can either choose to keep them, or simply delete them. <br/>
> I intend to contribute __________ _hours_ of computational time, and scrape a total of __________ _gigabytes_ of images. <br/>
> I have tested the most recent version of the program on my computer/preferred location (programming notebook, etc.), and after a few minutes of running a computing average speed, it prints "__________ images downloaded per second". <br/>

I will respond by sending a slightly modified copy of the Python file, adapted to data scrape a section of the database, with a size according to the amount of computational resources you stated were at your disposal and were willing to provide. Once this section is completed, send me the resulting "Images" folder compressed as a .zip file, and I will add your username to a new text file, credits.txt, alongside the amount of computational time you contributed.

Nearly 1 million images have been scraped in the last day, and I will be posting a section of these soon.

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

- __v1.6__: This version has been completed, I just forgot to post it. I'll do that soon. It fixes issue #1 from v1.5. v1.6 is the final version.
