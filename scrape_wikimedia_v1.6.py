pool = ThreadPool(processes = 10)

"""
def get_gray_categories(html):
  pattern = '"CategoryTreeEmptyBullet">► </span> <a href="/wiki/Category:.*" title="'
  finds = list(re.finditer(pattern, html))
  finds = [find.span() for find in finds]
  finds = [html[find[0]:find[1]] for find in finds]
  finds = [find.replace('"CategoryTreeEmptyBullet">► </span> <a href="/wiki/Category:', '').replace('" title="', '') for find in finds]
  return finds
"""

def get_categories(soup, html):
  """
  ungray_categories = [category.get('data-ct-title') for category in soup.find_all("span", {"class": "CategoryTreeToggle"})]
  gray_categories = get_gray_categories(html)
  return ungray_categories + gray_categories
  """

  text = soup.text
  issues = [find.span() for find in list(re.finditer("►  .*►  .*", text))]

  while len(issues) > 0:
    issue = issues[0]
    index = text[issue[0]:issue[1]][1:].index("►") + 1 + issue[0]
    text = text[:index] + "\n" + text[index:]

    issues = [find.span() for find in list(re.finditer("►  .*►  .*", text))]

  categories = [find[3:find.index(u"\u200e")] for find in re.findall("►  .*\n", text)]
  categories = [category.replace("/", "-") for category in categories]
  return categories

def lists_subcategories(html):
  return "<h2>Subcategories</h2>" in html

def parse_url_html(url):
  r = requests.get(url)
  html = r.content
  soup = BeautifulSoup(html, 'html.parser')
  return soup, str(html.decode())

def is_valid(url, all_image_urls):
  """
  if url in all_image_urls:
    return False
  else:
    if ".jpg" in url or ".png" in url or ".jpeg" in url:
      parsed = urlparse(url)
      return bool(parsed.netloc) and bool(parsed.scheme)
    else:
      return False
  """

  parsed = urlparse(url)
  return bool(parsed.netloc) and bool(parsed.scheme)

def extract_and_save_images(soup, all_image_urls, file_directory, indentation):
  # Save all images on current page to image folder
  urls = []
  for img in soup.find_all("img"):
    img_url = img.attrs.get("src")
    if not img_url:
      continue

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

      filepath_to_save = filepath_to_save.replace("/", "-")

      filepath_to_save = file_directory + filepath_to_save + ".jpg"
      filepath_to_save = filepath_to_save.replace("_", " ")

      global images_failed_so_far

      try:
        # urllib.request.urlretrieve(img_url, filepath_to_save)
        pool.apply_async(urllib.request.urlretrieve, (img_url, filepath_to_save))
        text_file = open("Sitemap.txt", "a")
        text_file.write("\t" * indentation + str(img_url) + "\n")
        text_file.close()
        global images_so_far
        images_so_far += 1
      except:
        images_failed_so_far += 1
        pass

      all_image_urls.append(img_url)

  os.system('clear')
  clear_output()
  print ("{num_images} images downloaded.".format(num_images = images_so_far))
  print ("{num_images} images failed.".format(num_images = images_failed_so_far))
  rate = images_so_far / (time.time() - start_time)
  print ("{rate} images downloaded per second.".format(rate = rate))

def make_site_map(url, directory, all_categories, indentation, all_image_urls):

  soup, html = parse_url_html(url)

  if lists_subcategories(html):
    categories = get_categories(soup, html)
    for category in categories:
      if category in directory:
        continue
      else:
        global num_categories_searched
        num_categories_searched += 1
        url = "https://commons.wikimedia.org/wiki/Category:" + category
        directory.append(category)
        indentation += 1
        file_directory = "Images/" + "/".join(directory) + "/"

        os.mkdir(file_directory.replace("_", " "))
        """
        try:
          os.mkdir(file_directory.replace("_", " "))
        except:
          print ("Failed to make the following directory: {dir_name}".format(dir_name = file_directory.replace("_", " ")))
        """

        all_categories.append(category)

        text_file = open("Sitemap.txt", "a")
        text_file.write("\t" * (indentation - 1) + category + "\n")
        text_file.close()

        make_site_map(url, directory, all_categories, indentation, all_image_urls)

        directory.pop()
        indentation -= 1

      file_directory = "Images/" + "/".join(directory) + "/"
      extract_and_save_images(soup, all_image_urls, file_directory, indentation)
  else:
    file_directory = "Images/" + "/".join(directory) + "/"
    extract_and_save_images(soup, all_image_urls, file_directory, indentation)

initial_url = "https://commons.wikimedia.org/wiki/Category:Categories"

directory = []
all_categories = []
all_image_urls = []
indentation = 0
images_so_far = 0
images_failed_so_far = 0
num_categories_searched = 0

start_time = time.time()
make_site_map(initial_url, directory, all_categories, indentation, all_image_urls)
end_time = time.time()

pool.close()
pool.join()