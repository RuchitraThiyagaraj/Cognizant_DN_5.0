from pages.checkbox_page import CheckboxPage


def test_checkbox_demo(driver):

    page = CheckboxPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/checkbox-demo/"
    )


    page.check_option(0)


    assert page.is_option_checked(0)