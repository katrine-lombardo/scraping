import os
import mechanicalsoup
import csv
from dotenv import load_dotenv

load_dotenv()

browser = mechanicalsoup.StatefulBrowser()


def extract_table_data(file_name):
    pass


def navigate():
    url = os.getenv("APARTMENT_URL")
    browser.open(url)
    print(browser.url)

    load_all_link = browser.page.select_one("button#load-all-units")
    print(load_all_link)


def handle_form():
    pass


def handle_pagination():
    pass


def main():
    navigate()
    handle_form()
    handle_pagination


main()
