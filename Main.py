import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
    time.sleep(2)
    enrolment_radio = driver.find_element(By.CSS_SELECTOR, "input[value='EID']")
    enrolment_radio.click()
    enrolment_input = driver.find_element(By.ID, "enrolment-id")
    enrolment_input.send_keys(enrolment_id)
    date_input = driver.find_element(By.ID, "eid-date")
    date_input.send_keys(eid_date)
    time_input = driver.find_element(By.ID, "eid-time")
    time_input.send_keys(eid_time)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(1000)
    print("Current URL:", driver.current_url)
finally:
    driver.quit()
