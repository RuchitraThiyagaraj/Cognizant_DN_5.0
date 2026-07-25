from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# open Selenium playground
driver.get("https://www.lambdatest.com/selenium-playground")

# clikc "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url
print("URL Assertion Passed")
print("CURRENT URL:",driver.current_url)

driver.back()
print("Navigated Back")

driver.execute_script('window.open("https://www.google.com");')
time.sleep(4)


# list all window handles
print("Window Handles:", driver.window_handles)
time.sleep(3)


#Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)


#print Google page title
print("Google Tab Title:", driver.title)
time.sleep(3)


#original tab
driver.switch_to.window(driver.window_handles[0])
time.sleep(4)


# take screenshot
driver.save_screenshot("playground_screenshot.png")
time.sleep(4)


# verify screenshot file exists
if os.path.exists("playground_screenshot.png"):
    print("Screenshot saved successfully.")
else:
    print("Screenshot not found.")

# get current window size
print("Current Window Size:", driver.get_window_size())

# Set new window size
driver.set_window_size(1280, 800)

# Consistent window size is important because websites are responsive
# Usin the same size ensures UI elements appear consistently during automation

time.sleep(3)

driver.quit()