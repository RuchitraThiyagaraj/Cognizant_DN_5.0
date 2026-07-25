from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_simple_form_demo(driver):

    driver.get(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )


    # Enter message
    message = driver.find_element(
        By.NAME,
        "my-text"
    )

    message.send_keys("Hello Selenium")


    # Click Submit
    submit = driver.find_element(
        By.CSS_SELECTOR,
        "button"
    )

    submit.click()


    # Wait for result
    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )


    # Verify
    assert result.text == "Received!"


def test_checkbox_demo(driver):

    driver.get(
        "https://the-internet.herokuapp.com/checkboxes"
    )


    checkbox = driver.find_elements(
        By.CSS_SELECTOR,
        "input[type='checkbox']"
    )[0]


    # Select checkbox
    checkbox.click()

    assert checkbox.is_selected()


    # Deselect checkbox
    checkbox.click()

    assert not checkbox.is_selected()