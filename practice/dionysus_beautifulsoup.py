# 1. Pip install Beautiful Soup:
##    $ python -m pip install beautifulsoup4


# 2. Create a BeautifulSoup object
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


# 3. Use a BeautifulSoup object
# Run the program and enter REPL:
##     >>> python -i dionysus_beautifulsoup.py

# Print all HTML text on the page:
##     >>> print(soup.get_text())

# Return a list of all <img> tags:
##     >>> soup.find_all("img")

# Unpack tag objects:
##     >>> image1, image2 = soup.find_all("img")

# Get tag's name property
##     >>> image1.name

# Get tag's src property
##     >>> image1["src"]
##     >>> image2["src"]

# Get cleaned up title tag in a document
##     >>> soup.title

# Get title tag text
##     >>> soup.title.string

# Find all the <img> tags that have a src attribute equal to the value
# /static/dionysus.jpg
##     >>> soup.find_all("img", src="/static/dionysus.jpg")
