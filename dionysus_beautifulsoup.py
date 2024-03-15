# 1. Pip install Beautiful Soup:
##      $ python -m pip install beautifulsoup4


# 2. Create a BeautifulSoup object
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


# 3. Use a BeautifulSoup object
