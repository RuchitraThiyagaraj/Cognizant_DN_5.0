import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_demo(driver, base_url, message):

    driver.get(
        base_url + "simple-form-demo/"
    )


    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "user-message")
        )
    )


    input_box.clear()

    input_box.send_keys(message)


    button = driver.find_element(
        By.ID,
        "showInput"
    )

    button.click()


    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "message")
        )
    )


    assert result.get_attribute("textContent") == message




def test_checkbox_demo(driver, base_url):

    driver.get(
        base_url + "checkbox-demo/"
    )


    checkbox = driver.find_element(
        By.CSS_SELECTOR,
        "input[type='checkbox']"
    )


    checkbox.click()

    assert checkbox.is_selected()


    checkbox.click()

    assert not checkbox.is_selected()




def test_dropdown_selection(driver, base_url):

    driver.get(
        base_url + "select-dropdown-demo/"
    )


    dropdown_element = driver.find_element(
        By.ID,
        "select-demo"
    )


    dropdown = Select(
        dropdown_element
    )


    dropdown.select_by_visible_text(
        "Wednesday"
    )


    selected_option = dropdown.first_selected_option.text


    assert selected_option == "Wednesday"