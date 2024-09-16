from selenium.webdriver.common.by import By

cart_icon_loc = (By.XPATH, '//span[text()="My Cart"]')
empty_cart_icon_loc = (
    By.XPATH, '//strong[text()="You have no items in your shopping cart."]'
)
not_empty_cart_icon_loc = (By.XPATH, '//*[contains(@class, "counter-number")]')
product_loc = (By.XPATH, '//*[@alt="Ana Running Short"]')
product_size_loc = (By.XPATH, '//*[@id="option-label-size-143-item-171"]')
product_color_loc = (By.XPATH, '//*[@id="option-label-color-93-item-49"]')
add_to_cart_button_loc = (By.XPATH, '//button[@title="Add to Cart"]')
product_name_loc = (By.TAG_NAME, 'h1')
add_to_compare_loc = (By.CLASS_NAME, 'tocompare')
added_to_compare_message_loc = (
    By.XPATH, '//*[contains(@data-bind, "prepareMessageForHtml")]'
)
compare_section_loc = (By.CSS_SELECTOR, 'div.sidebar.sidebar-additional')
product_in_compare_loc = (By.XPATH, '//*[@id="compare-items"]')
