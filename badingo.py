# Building my first scraper!

# 1. Extract HTML

from urllib.request import urlopen

url = "https://badingo.net"
page = urlopen(url)
print(page)


html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# 2. Extract string from HTML

