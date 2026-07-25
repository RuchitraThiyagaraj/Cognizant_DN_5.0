"""
Selenium Components:

1. WebDriver:
WebDriver is an API that allows Selenium to communicate with browsers.
It sends commands from the Selenium script to the browser and controls actions
like opening pages, clicking buttons, and entering data.

2. Selenium Grid:
Selenium Grid allows tests to run in parallel on different machines,
browsers, and operating systems. It reduces execution time for large test suites.

3. Selenium IDE:
Selenium IDE is a record and playback tool used to create automation scripts
without writing much code. It can also generate test code.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()

# Running Chrome in headless mode means browser runs without opening a window
options.add_argument("--headless")


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait applies globally to all elements.
# It is considered bad practice because it can slow down tests and gives less
# control compared to explicit waits for specific elements.

driver.implicitly_wait(10)


driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

driver.quit()