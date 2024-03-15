# Write a program that grabs the full HTML from the following URL:
# url = "http://olympus.realpython.org/profiles/dionysus"
# Then use .find() to display the text following Name: and Favorite Color: (not including any leading spaces or trailing HTML tags that might appear on the same line).

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

# Find the title
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)
print(title)

# Find the name and favourite colour
for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html[text_start_idx:text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)
