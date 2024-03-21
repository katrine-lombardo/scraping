import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    load_dotenv()
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    return driver


def navigate_to_url(driver, url):
    driver.get(url)


def close_modal(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-modal-close")))
    close_button = driver.find_element(By.CLASS_NAME, "ant-modal-close")
    close_button.click()
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ant-modal-root")))


def click_load_all_button(driver):
    wait = WebDriverWait(driver, 20)
    load_all_button = driver.find_element(By.ID, "load-all-units")
    wait.until(EC.element_to_be_clickable((By.ID, "load-all-units")))
    driver.execute_script("arguments[0].scrollIntoView();", load_all_button)
    actions = ActionChains(driver)
    actions.move_to_element(load_all_button).click().perform()


def wait_for_units_to_load(driver):
    try:
        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.ID, "load-all-units"))
        )
        print("All units have loaded.")
    except TimeoutException:
        print("Timeout waiting for units to load.")


def process_apt_elements(driver):
    apt_elements = driver.find_elements(By.CLASS_NAME, "unit-item-details")
    print("number of units: ", len(apt_elements))
    for apt_element in apt_elements:
        process_apt_element(apt_element)


def process_apt_element(apt_element):
    unit_info = apt_element.find_element(By.CLASS_NAME, "ant-card-meta-title")
    unit_info_parts = unit_info.text.strip().split()
    unit_number = unit_info_parts[1] if len(unit_info_parts) > 1 else ""
    location = unit_info_parts[2] if len(unit_info_parts) > 1 else ""
    print(unit_number)
    print(location)

    term_info = apt_element.find_element(By.CLASS_NAME, "term-length")
    term_parts = term_info.text.strip().split()
    term_length_months = term_parts[1] if len(term_parts) > 1 else ""
    print(term_length_months)

    available_date = apt_element.find_element(By.CLASS_NAME, "available-date")
    print(available_date.text.strip())

    unit_price = apt_element.find_element(By.CLASS_NAME, "unit-price")
    print(unit_price.text.strip())

    description = apt_element.find_element(By.CLASS_NAME, "description")
    description_parts = description.text.strip().split()
    bedrooms = description_parts[0] if len(description_parts) > 1 else ""
    bathrooms = description_parts[3] if len(description_parts) > 1 else ""
    sqft = description_parts[6] if len(description_parts) > 1 else ""
    print(bedrooms)
    print(bathrooms)
    print(sqft)

    details_link = apt_element.find_element(By.TAG_NAME, "a")
    unit_url = details_link.get_attribute("href")
    print(unit_url)


def main():
    driver = setup_driver()
    url = os.getenv("APARTMENT_URL")
    navigate_to_url(driver, url)
    close_modal(driver)
    click_load_all_button(driver)
    wait_for_units_to_load(driver)
    process_apt_elements(driver)
    driver.quit()


if __name__ == "__main__":
    main()
