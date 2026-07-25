import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():

    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Teardown
    driver.quit()