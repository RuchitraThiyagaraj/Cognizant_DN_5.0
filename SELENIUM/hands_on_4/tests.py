from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://learner.saveetha.in")
time.sleep(5)
print(driver.title)

driver.quit()