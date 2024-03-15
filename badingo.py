# Building my first scraper!
from urllib.request import urlopen


# 1. Extract HTML
url = "https://badingo.net"
page = urlopen(url)
print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)


# 2. Extract string from HTML
title_index = html.find("<title>")
print(title_index)

start_index = title_index + len("<title>")
print(start_index)

end_index = html.find("</title>")
print(end_index)

title = html[start_index:end_index]
print(title)
