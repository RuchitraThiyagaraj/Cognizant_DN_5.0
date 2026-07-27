from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver):

    page = DropdownPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/select-dropdown-demo/"
    )

    page.select_day("Monday")