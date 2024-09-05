import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

enrolment_id = "12345678901234"
eid_date = "2023-09-01"
eid_time = "12:30:AM"

url = "http://127.0.0.1:5500/index.html"
chrome_driver_path = r"C:\Users\Hrithik\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

chrome_options = Options()
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get(url)
    actions = ActionChains(driver)

    enrolment_radio = driver.find_element(By.CSS_SELECTOR, "input[value='EID']")
    actions.move_to_element(enrolment_radio).click().perform()

    enrolment_input = driver.find_element(By.ID, "enrolment-id")
    actions.move_to_element(enrolment_input).click().send_keys(enrolment_id).perform()

    date_input = driver.find_element(By.ID, "eid-date")
    actions.move_to_element(date_input).click().send_keys(eid_date).perform()

    time_input = driver.find_element(By.ID, "eid-time")
    actions.move_to_element(time_input).click().send_keys(eid_time).perform()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    actions.move_to_element(submit_button).click().perform()

    time.sleep(1000)
    print("Current URL after submission:", driver.current_url)

finally:
    driver.quit()
