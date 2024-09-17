from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError(
                'Page can not be opened for this page class'
            )

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def check_header_text(self, title):
        h1_name_loc = (By.TAG_NAME, 'h1')
        h1_element = self.find(h1_name_loc)
        assert h1_element.text == title
