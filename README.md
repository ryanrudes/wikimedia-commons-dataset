# Wikimedia Commons Image Dataset
<ins>The Largest Image Dataset For Machine Learning</ins>

Wikimedia Commons is an online repository of openly-available media files, such as image, audio, video, and JSON files. You may view the current quantity of available content [here](https://commons.wikimedia.org/wiki/Special:MediaStatistics).

As of June 24, 2020, the database consists of approximately 56.47 million files of image content of file format .jpg, .jpeg, or .png.

The size of the dataset provides vast potential for use in machine learning. Another benefit is the detailed categorization of the contents of this media collection, allowing for rather simple data extraction for supervised learning methods.

There does, indeed, exist an API for data scraping Wikipedia Commons, however, it introduces an unsatisfying limit of 500 files at a time.

This Python script, however, recursively iterates over all categories and subcategories of the Wikipedia Commons image dataset, extracting all valid images, and saving them approperiately in identically organized folders.

The speed of content extracting matches, and potentially surpasses the rate of the official Wikipedia Commons Python API, thus providing benefits towards computational time required.

Although this method of extraction is faster, the dataset is <b>vast</b>, and therefore, the process is certainly <b>not</b> rapid.

Depending upon the computational power at your availability, the time required will vary greatly, however, it appears to collect nearly one thousand images, labeled and categorized approperiately, every minute and a half to three minutes.

Once the dataset is fully completed, I will compress it into a zip file, and add it to this repo. In the meanwhile, feel free to do some datascraping yourself.

Setup is fairly simple. cd to the approperiate directory, then install the required packages (if they are not installed already on your machine) with: ```pip3 install -r requirements.txt```

Then, all you must do to run the data scraper is, of course, ```python3 scrape_wikimedia.py```.

When the program begins (note that it will not print anything to the console), you will notice subdirectories beginning to appear within the "Images" folder. Over time, these subdirectories will be filled with images cooresponding to the description provided by each particular folder's name. This organization is identical to that of the Wikimedia Commons content collection, which you can view [here](https://commons.wikimedia.org/wiki/Category:Categories).

Enjoy!
