import requests
import re
from urllib.parse import urljoin, urlparse
import os
import time
import urllib
from bs4 import BeautifulSoup

def get_categories(soup):
  return [category.get('data-ct-title') for category in soup.find_all("span", {"class": "CategoryTreeToggle"})]

def lists_subcategories(html):
  return "<h2>Subcategories</h2>" in html

def parse_url_html(url):
  r = requests.get(url)
  html = r.content
  soup = BeautifulSoup(html, 'html.parser')
  return soup, str(html.decode())

def is_valid(url, all_image_urls):
  if url in all_image_urls:
    return False
  else:
    if ".jpg" in url or ".png" in url or ".jpeg" in url:
      parsed = urlparse(url)
      return bool(parsed.netloc) and bool(parsed.scheme)
    else:
      return False

def extract_and_save_images(soup, all_image_urls, file_directory, images_so_far):
  # Save all images on current page to image folder
  urls = []
  for img in soup.find_all("img"):
    img_url = img.attrs.get("src")
    if not img_url:
      # if img does not contain src attribute, just skip
      continue

    # make the URL absolute by joining domain with the URL that is just extracted
    img_url = urljoin(file_directory, img_url)

    try:
      pos = img_url.index("?")
      img_url = img_url[:pos]
    except ValueError:
      pass

    # finally, if the url is valid
    if is_valid(img_url, all_image_urls):
        
      index = img_url[::-1].index("/")
      filepath_to_save = img_url[len(img_url) - index:]
      filepath_to_save = filepath_to_save[:filepath_to_save.index(".")]

      if "%" in filepath_to_save:
        filepath_to_save = filepath_to_save[:filepath_to_save.index("%")]

      filepath_to_save = file_directory + filepath_to_save + ".jpg"
      filepath_to_save = filepath_to_save.replace("_", " ")

      try:
        urllib.request.urlretrieve(img_url, filepath_to_save)
      except:
        pass

      images_so_far += 1
      all_image_urls.append(img_url)

def make_site_map(url, directory, all_categories, indentation, all_image_urls, images_so_far):

  soup, html = parse_url_html(url)

  if lists_subcategories(html):
    categories = get_categories(soup)
    for category in categories:
      if category in directory:
        continue
      else:
        url = "https://commons.wikimedia.org/wiki/Category:" + category
        directory.append(category)
        indentation += 1
        file_directory = "Images/" + "/".join(directory) + "/"
        os.mkdir(file_directory.replace("_", " "))
        all_categories.append(category)

        text_file = open("Sitemap.txt", "a")
        text_file.write("\t" * indentation + category + "\n")
        text_file.close()

        make_site_map(url, directory, all_categories, indentation, all_image_urls, images_so_far)

        directory.pop()
        indentation -= 1

      file_directory = "Images/" + "/".join(directory) + "/"
      extract_and_save_images(soup, all_image_urls, file_directory, images_so_far)
  else:
    file_directory = "Images/" + "/".join(directory) + "/"
    extract_and_save_images(soup, all_image_urls, file_directory, images_so_far)

initial_url = "https://commons.wikimedia.org/wiki/Category:Categories"

directory = []
all_categories = []
all_image_urls = []
indentation = 0
images_so_far = 0

make_site_map(initial_url, directory, all_categories, indentation, all_image_urls, images_so_far)