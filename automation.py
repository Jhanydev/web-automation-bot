
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("Starting Web Automation...")

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python automation")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()

print("Automation finished.")
