import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install, options=options())
)

url = os.getenv("APARTMENT_URL")

driver.get(url)
apt_elements = driver.find_elements(By.CLASS_NAME, "unit-item-details")
for apt_element in apt_elements:
    available_date = apt_element.find_element("div", class_="available-date")
    print(available_date.text.strip())
