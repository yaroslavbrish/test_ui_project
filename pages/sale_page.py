from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import sale_locators as loc
from selenium.webdriver.support import expected_conditions as ec


class SalePage(BasePage):
    page_url = '/sale.html'

    def women_sale(self):
        women_sale = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(loc.women_sale_loc)
        )
        women_sale.click()

    def men_sale(self):
        men_sale = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(loc.men_sale_loc)
        )
        men_sale.click()

    def gear(self):
        gear = WebDriverWait(self.driver, 5).until(
            ec.element_to_be_clickable(loc.gear_loc)
        )
        gear.click()
