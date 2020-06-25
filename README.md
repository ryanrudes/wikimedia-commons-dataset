# Wikimedia Commons Image Dataset

<ins>The most oragnized image dataset for machine learning.</ins>

Wikimedia Commons is an online repository of openly-available media files, such as image, audio, video, and JSON files. You may view the current quantity of available content [here](https://commons.wikimedia.org/wiki/Special:MediaStatistics).

As of June 24, 2020, the database consists of approximately 56.47 million files of image content of file format .jpg, .jpeg, or .png.

The size of the dataset provides vast potential for use in machine learning. Another benefit is the detailed categorization of the contents of this media collection, allowing for rather simple data extraction for supervised learning methods. In summary, the benefits of this dataset are fantastic organization of classes, wide variety of features, and a large number of images.

There does, indeed, exist an API for data scraping Wikipedia Commons, however, it introduces an unsatisfying limit of 500 files at a time.

This Python script, however, recursively iterates over all categories and subcategories of the Wikipedia Commons image dataset, extracting all valid images, and saving them approperiately in identically organized folders.

The speed of content extracting matches, and likely surpasses the rate of the official Wikipedia Commons Python API, thus providing benefits towards computational time required. On a Google Colab high-RAM runtime, it averages 14-17 images, downloaded, labeled, and categorized approperiately, each second.

Although this method of extraction and download is faster, the dataset is still <b>vast</b>, and therefore, the process is certainly <b>not</b> rapid.

Once the dataset is fully completed, I will compress it into a zip file, and add it to this repo. In the meanwhile, feel free to do some datascraping yourself, or, if you'd like to contribute computational resources, see below*.

Setup is fairly simple:
1.  cd to the approperiate directory, then install the required packages (if they are not installed already on your machine) with: ```pip3 install -r requirements.txt```
2.  Next, create an empty folder, titled "Images", inside of the directory.
3.  Finally, of course, you must run this command to begin data scraping ```python3 scrape_wikimedia.py``` (or the approperiate filename, once additional versions are added to this repo).

When the program begins (note that if you are running v1.0, it will not print anything to the console), you will notice subdirectories beginning to appear within the "Images" folder. In addition, a text file, titled "Sitemap.txt" will appear in the directory, which will contain the categories, with each additional subcategory indented approperiately. Over time, these subdirectories will become filled with images corresponding to the description provided by each particular folder's name. This organization of image content is identical to that of the Wikimedia Commons collection, which you can view [here](https://commons.wikimedia.org/wiki/Category:Categories).

*If you would like to contribute computational resources to this effort, simply message me at my preferred email address (ryanrudes@gmail.com), which is listed on my Github profile.
I will respond by sending a slightly modified copy of the Python file, adapted to data scrape just a single major category. Once this category is completed, send me the Images folder compressed as a .zip file, and I will add your username to a new text file, credits.txt, alongside the amount of computational time you contributed.
