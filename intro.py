# Building my first scraper!
from urllib.request import urlopen
import re


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


# 3. Working with Regular Expressions: Metacharacters

## Asterix(*) stands for zero or more instances
print(re.findall("ab*c", "ac"))
print(re.findall("ab*c", "abcd"))
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abdc"))
print(re.findall("ab*c", "ABC"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))

## Period(.) stands for any single character
print(re.findall("a.c", "abc"))
print(re.findall("a.c", "abbc"))
print(re.findall("a.c", "ac"))
print(re.findall("a.c", "acc"))

## Pattern (.*) stands for any character repeated any number of times
print(re.findall("a.*c", "abc"))
print(re.findall("a.*c", "abbc"))
print(re.findall("a.*c", "ac"))
print(re.findall("a.*c", "acc"))


# 4. MatchObject

## re.search() returns every possible result
## MatchObject.group() returns the first and most inclusive result
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(match_results.group())

## Greedy pattern: re.sub() replaces text in a string
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

## Non-greedy pattern(*?) matches the shortest possible string of text
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)


# 5. Extract text from HTML with regular expressions
## Go to dionysus_regex.py


# 6. Using a HTML parser for web scraping
## Go to profiles_beautifulsoup.py


# 7. Interact with HTML forms using a headless browser
## Install MechanicalSoup: python -m pip install MechanicalSoup
## Go to olympus_mechanicalsoup.py


# 8. Interact with sites in real time
## Use .sleep() from Python's time module to pause
import time

print("I'm about to wait for five seconds...")
time.sleep(5)
print("Done waiting!")

## Use range and if statement to stop after x requests

for i in range(4):
    # <Code here>

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)
