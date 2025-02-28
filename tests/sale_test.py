import pytest


@pytest.mark.smoke
def test_open_women_sale_page(sale_page):
    sale_page.open_page()
    sale_page.women_sale()
    sale_page.check_header_text("Women Sale")


@pytest.mark.regression
def test_open_men_sale_page(sale_page):
    sale_page.open_page()
    sale_page.men_sale()
    sale_page.check_header_text("Men Sale")


@pytest.mark.regression
def test_open_gear_page(sale_page):
    sale_page.open_page()
    sale_page.gear()
    sale_page.check_header_text("Gear")
