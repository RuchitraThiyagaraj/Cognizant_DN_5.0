from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.youtube.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Cognizant Digital Nurture 5.0")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

driver.find_element(
    By.CSS_SELECTOR,
    "a#video-title"
).click()

time.sleep(5)

driver.quit()