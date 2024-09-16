import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account_page import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
