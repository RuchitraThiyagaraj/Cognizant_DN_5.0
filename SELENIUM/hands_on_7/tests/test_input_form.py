from pages.input_form_page import InputFormPage


def test_input_form_submit(driver):

    page = InputFormPage(driver)

    page.navigate_to(
        "https://www.testmuai.com/selenium-playground/input-form-demo/"
    )

    page.fill_form(
        "Ruchitra",
        "test@gmail.com",
        "9876543210",
        "Chennai"
    )

    page.submit_form()