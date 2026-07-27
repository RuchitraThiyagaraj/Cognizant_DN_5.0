from pages.simple_form_page import SimpleFormPage


def test_simple_form_submission(driver):

    page = SimpleFormPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/simple-form-demo/"
    )


    page.enter_message(
        "Hello Selenium"
    )

    page.click_submit()


    assert page.get_displayed_message() == "Hello Selenium"