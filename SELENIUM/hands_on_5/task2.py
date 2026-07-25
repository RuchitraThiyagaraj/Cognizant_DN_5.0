from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground")

wait = WebDriverWait(driver, 10)


#task 36: Wait for Success Alert

# Clikc Alerts Demo
wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Bootstrap Alerts")
    )
).click()


# Click Success Message button
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Success Message')]")
    )
).click()


# Wait until success alert becomes visible
success_alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)


# Assert alert text
print(success_alert.text)
assert "success" in success_alert.text.lower()

print("Success alert assertion passed")




# Task 37: sleep() vs Explicit Wait


# Using time.sleep()

start = time.time()

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Success Message')]")
    )
).click()

time.sleep(3)

alert = driver.find_element(
    By.CSS_SELECTOR,
    ".alert-success"
)

sleep_time = time.time() - start

print("time.sleep() execution time:", sleep_time)



# Using WebDriverWait

start = time.time()

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Success Message')]")
    )
).click()


wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".alert-success")
    )
)

explicit_time = time.time() - start

print("Explicit wait execution time:", explicit_time)



# expkaination
# time.sleep() always waits the fixed amount of time.
# WebDriverWait continues immediately when condition is satisfied.
# Explicit wait is faster on fast systems and reliable on slow systems.



# Task 38: element_to_be_clickable()

# visibility_of_element_located:
# Element exists and is visible.

# element_to_be_clickable:
# Element is visible + enabled + not blocked by another element.


button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Success Message')]")
    )
)

button.click()

print("Button clicked successfully")



# Task 39: FluentWait Concept

# FluentWait allows: Custom polling interval , Ignoring exceptions ,Maximum timeout

# Task 39: FluentWait Concept

# Open a page with a table
driver.get("https://www.testmuai.com/selenium-playground/table-pagination-demo")

from selenium.common.exceptions import NoSuchElementException

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

row = fluent_wait.until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "table tbody tr")
    )
)

print("Table row loaded")

time.sleep(3)
driver.quit()

'''
TimeoutException occurred because Selenium waited for 10 seconds, but the table row (table tbody tr) was not found on the current page. So, another page was used.'''