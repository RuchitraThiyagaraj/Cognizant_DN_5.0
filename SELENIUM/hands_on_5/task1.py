#------------------------------------------
#Locator Preference Ranking
#------------------------------------------

#1. ID
#Best choice because IDs are usually unique.
#It is fast and easy to read.

#2. NAME
#Good if the name is unique.
#Mostly used for form elements.

#3. CSS_SELECTOR
#Fast and flexible.
#Can locate elements using id, class and attributes.

#4. Relative XPath
#Useful when ID or NAME is not available.
#Can locate elements using text(), contains() and multiple attributes.

#5. CLASS_NAME
#Works only if the class is unique.
#Many elements can have the same class.

#6. TAG_NAME
#Least preferred because many elements have the same tag.
#It usually returns the first matching element.

#Absolute XPath
#Avoid using it because it breaks if the HTML structure changes.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()


# Open LambdaTest Playground
driver.get("https://www.lambdatest.com/selenium-playground")

time.sleep(3)


# Click Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

time.sleep(3)


# verify URL
assert "simple-form-demo" in driver.current_url

print("URL Assertion Passed")
print("Current URL:", driver.current_url)



# LOCATOR STRATEGIES

# Locate message input using ID

message = driver.find_element(By.ID, "user-message")
message.send_keys("Testing Selenium ID")

time.sleep(2)



# NAME

message = driver.find_element(By.NAME, "message")
print("NAME locator works")



# CLASS_NAME

message = driver.find_element(By.CLASS_NAME, "form-control")
print("CLASS_NAME locator works")


# TAG_NAME

message = driver.find_element(By.TAG_NAME, "input")
print("TAG_NAME locator works")



# XPATH Absolute




message = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)

print("Absolute XPath works")




# Relative XPath using attribute

message = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("Relative XPath works")


# CSS SELECTORS


# By ID

message = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

print("CSS ID works")



# By attribute

message = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)
print("CSS attribute works")



# Parent child relationship
message = driver.find_element(
    By.CSS_SELECTOR,
    "div > input"
)

print("CSS parent-child works")


# CHECKBOX DEMO

#go to the prev page
driver.back()

driver.find_element(
    By.LINK_TEXT,
    "Checkbox Demo"
).click()





# XPath text()

checkbox = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("XPath text() works")



# XPath contains()

checkboxes = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("Number of options:", len(checkboxes))



# SCREENSHOT


driver.save_screenshot("lambda_test.png")


if os.path.exists("lambda_test.png"):
    print("Screenshot saved")



# Window size

print(
    "Window Size:",
    driver.get_window_size()
)


driver.set_window_size(1280,800)




driver.quit()