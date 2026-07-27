from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.ID, "name")
    COMPANY = (By.ID, "company")

    EMAIL = (By.ID, "inputEmail4")
    PASSWORD = (By.ID, "inputPassword4")

    WEBSITE = (
        By.XPATH,
        "//input[@placeholder='Website']"
    )

    COUNTRY = (
        By.XPATH,
        "//select[@name='country']"
    )

    CITY = (By.ID, "inputCity")

    ADDRESS1 = (By.ID, "inputAddress1")
    ADDRESS2 = (By.ID, "inputAddress2")

    STATE = (By.ID, "inputState")
    ZIP = (By.ID, "inputZip")

    SUBMIT = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )


    def fill_form(self, name, email, phone, city):

        # Name
        self.wait_for_element(
            self.NAME
        ).send_keys(name)


        # Company
        self.wait_for_element(
            self.COMPANY
        ).send_keys("Cognizant")


        # Email
        self.wait_for_element(
            self.EMAIL
        ).send_keys(email)


        # Password
        self.wait_for_element(
            self.PASSWORD
        ).send_keys("Password123")


        # Website
        self.wait_for_element(
            self.WEBSITE
        ).send_keys("https://example.com")


        # Country dropdown
        country = self.wait_for_element(
            self.COUNTRY
        )

        Select(country).select_by_visible_text(
            "United States"
        )


        # City
        self.wait_for_element(
            self.CITY
        ).send_keys(city)


        # Address 1
        self.wait_for_element(
            self.ADDRESS1
        ).send_keys("Chennai")


        # Address 2
        self.wait_for_element(
            self.ADDRESS2
        ).send_keys("Tamil Nadu")


        # State
        self.wait_for_element(
            self.STATE
        ).send_keys("Tamil Nadu")


        # Zip Code
        self.wait_for_element(
            self.ZIP
        ).send_keys("600001")


    def submit_form(self):

        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.SUBMIT
            )
        )

        button.click()