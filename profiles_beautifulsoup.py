"""
Write a program that grabs the full HTML from the page at the URL
http://olympus.realpython.org/profiles.

Using Beautiful Soup, print out a list of all the links on the page by looking
for HTML tags with the name a and retrieving the value taken on by the href
attribute of each tag.

The final output should look like this:

http://olympus.realpython.org/profiles/aphrodite
http://olympus.realpython.org/profiles/poseidon
http://olympus.realpython.org/profiles/dionysus

Make sure that you only have one slash (/) between the base URL and the relative
URL.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
    link_url = base_url + link["href"]
    print(link_url)
