from selenium.webdriver.common.by import By


first_name_loc = (By.XPATH, '//*[@id="firstname"]')
last_name_loc = (By.XPATH, '//*[@id="lastname"]')
email_loc = (By.XPATH, '//*[@id="email_address"]')
password_loc = (By.XPATH, '//*[@id="password"]')
confirm_password_loc = (By.XPATH, '//*[@id="password-confirmation"]')
create_button_loc = (By.XPATH, '//button[@title="Create an Account"]')
alert_loc = (By.XPATH, '//*[contains(@data-bind, "prepareMessageForHtml")]')
password_strength_loc = (By.XPATH, '//*[@id="password-strength-meter-label"]')
header_name_loc = (By.TAG_NAME, 'h1')
