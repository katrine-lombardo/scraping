import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)


url = os.getenv("APARTMENT_URL")
driver.get(url)


wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-modal-close")))
close_button = driver.find_element(By.CLASS_NAME, "ant-modal-close")
close_button.click()


load_all_button = driver.find_element(By.ID, "load-all-units")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "load-all-units")))
driver.execute_script("arguments[0].scrollIntoView();", load_all_button)
actions = ActionChains(driver)
actions.move_to_element(load_all_button).click().perform()

apt_elements = driver.find_elements(By.CLASS_NAME, "unit-item-details")
for apt_element in apt_elements:
    available_date = apt_element.find_element(By.CLASS_NAME, "available-date")
    print(available_date.text.strip())

driver.quit()
