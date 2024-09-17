from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def click_on_product_card(self):
        product = self.find(loc.product_loc)
        product.click()

    def add_to_compare(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        first_product = wait.until(
            ec.presence_of_element_located(loc.product_loc)
        )
        add_to_compare = self.find(loc.add_to_compare_loc)
        actions.move_to_element(first_product).click(add_to_compare).perform()

    def check_item_is_added_to_compare(self):
        wait = WebDriverWait(self.driver, 5)
        compare_section_item = wait.until(
            ec.presence_of_element_located(loc.compare_section_loc)
        )
        product_in_compare = compare_section_item.find_element(
            *loc.product_in_compare_loc
        )
        assert product_in_compare is not None, \
            "Товар не был добавлен к сравнению"

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        actions = ActionChains(self.driver)
        first_product = wait.until(
            ec.presence_of_element_located(loc.product_loc)
        )
        product_size = wait.until(
            ec.presence_of_element_located(loc.product_size_loc)
        )
        product_color = wait.until(
            ec.presence_of_element_located(loc.product_color_loc)
        )
        add_to_cart_button = wait.until(
            ec.presence_of_element_located(loc.add_to_cart_button_loc)
        )
        actions.move_to_element(first_product)
        actions.click(product_size)
        actions.click(product_color)
        actions.click(add_to_cart_button)
        actions.perform()

    def check_item_is_added_to_cart(self):
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element(
                loc.not_empty_cart_icon_loc, '1'
            )
        )
