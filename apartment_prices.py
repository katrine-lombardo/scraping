import os
import mechanicalsoup
from dotenv import load_dotenv

load_dotenv()

browser = mechanicalsoup.Browser()
apartment_url = os.getenv("APARTMENT_URL")
html_page = browser.get(apartment_url)
html_text = html_page.soup
print(html_text)
