import pytest
from selenium import webdriver


# Browser fixture
@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()



# Base URL fixture
@pytest.fixture(scope="session")
def base_url():

    return "https://www.lambdatest.com/selenium-playground/"



# Screenshot on failure hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()


    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            test_name = item.name

            driver.save_screenshot(
                f"{test_name}_failure.png"
            )