from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class CreateAccount(BasePage):
    page_url = '/customer/account/create'

    def enter_first_name(self, first_name):
        first_name_field = self.find(loc.first_name_loc)
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.find(loc.last_name_loc)
        last_name_field.send_keys(last_name)

    def enter_email(self, email):
        email_field = self.find(loc.email_loc)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find(loc.password_loc)
        # password_field.send_keys(password)
        actions = ActionChains(self.driver)
        actions.click(password_field).send_keys(password).perform()

    def confirm_password(self, password):
        confirm_password_field = self.find(loc.confirm_password_loc)
        # confirm_password_field.send_keys(password)
        actions = ActionChains(self.driver)
        actions.click(confirm_password_field).send_keys(password).perform()

    def click_button(self):
        self.find(loc.create_button_loc).click()

    def check_alert_appears(self):
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element(
                loc.alert_loc,
                "There is already an account with this email address"
            )
        )

    def check_password_is_weak(self, password):
        self.enter_password(password)
        self.confirm_password(password)
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element(
                loc.password_strength_loc, "Weak"
            )
        )
