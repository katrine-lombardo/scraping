import os
import mechanicalsoup
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("APARTMENT_URL")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="community-unit-listings")
# print(results.prettify())

apt_elements = results.find_all("div", class_="unit-item-details")
for apt_element in apt_elements:
    unit_info = apt_element.find("div", class_="ant-card-meta-title")
    unit_info_parts = unit_info.text.strip().split()
    unit_number = unit_info_parts[1] if len(unit_info_parts) > 1 else ""
    location = unit_info_parts[2] if len(unit_info_parts) > 1 else ""
    print(unit_number)
    print(location)

    term_info = apt_element.find("span", class_="term-length")
    term_parts = term_info.text.strip().split()
    term_length_months = term_parts[1] if len(term_parts) > 1 else ""
    print(term_length_months)

    available_date = apt_element.find("div", class_="available-date")
    print(available_date.text.strip())

    unit_price = apt_element.find("span", class_="unit-price")
    print(unit_price.text.strip())

    description = apt_element.find("div", class_="description")
    description_parts = description.text.strip().split()
    bedrooms = description_parts[0] if len(description_parts) > 1 else ""
    bathrooms = description_parts[3] if len(description_parts) > 1 else ""
    sqft = description_parts[6] if len(description_parts) > 1 else ""
    print(bedrooms)
    print(bathrooms)
    print(sqft)

    apply_link = apt_element.find_all("a")[0]["href"]
    print(apply_link)
    print()
