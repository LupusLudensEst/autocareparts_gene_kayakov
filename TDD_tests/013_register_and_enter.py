from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
CLICK_ON_CREATE_ACCOUNT = (By.XPATH, "(//a[@id='customer_register_link'])[1]")
FIRST_NAME_REG = (By.ID, "first_name")
LAST_NAME_REG = (By.ID, "last_name")
EMAIL_REG = (By.ID, "email")
PASSWORD_REG = (By.ID, "create_password")
CREATE_BUTTON = (By.XPATH, "//input[@value='Create']")
I_AM_NOT_ROBOT = (By.CSS_SELECTOR, "div.recaptcha-checkbox-border")
SUBMIT_BTN = (By.XPATH, "//input[@value='Submit']")
TEXT_AFTER_SUBMIT_BTN = (By.XPATH, "//ul[@class='shopify-challenge__error']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# Activate ActionChains
action = ActionChains(driver)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Click on Create an Account button
wait.until(EC.element_to_be_clickable(CLICK_ON_CREATE_ACCOUNT)).click()

# 3. Fill First Name field
password = str(randint(1000000000, 9999999999))
name = 'name' + "_" + password
last_name = name + "_" + password
email = (name + '@sample.com')
print(f'\nName: {name}, \nlast name: {last_name},\nemail: {email} \nand password: {password}')

wait.until(EC.presence_of_element_located(FIRST_NAME_REG)).clear()
wait.until(EC.presence_of_element_located(FIRST_NAME_REG)).send_keys(name)

# 4. Fill Last Name field
wait.until(EC.presence_of_element_located(LAST_NAME_REG)).clear()
wait.until(EC.presence_of_element_located(LAST_NAME_REG)).send_keys(last_name)

# 5. Fill Email field
wait.until(EC.presence_of_element_located(EMAIL_REG)).clear()
wait.until(EC.presence_of_element_located(EMAIL_REG)).send_keys(email)

# 6. Fill Password field
wait.until(EC.presence_of_element_located(PASSWORD_REG)).clear()
wait.until(EC.presence_of_element_located(PASSWORD_REG)).send_keys(password)

# 7. Click on Create button
wait.until(EC.element_to_be_clickable(CREATE_BUTTON)).click()

# 8. Click on Submit button and verify text is here
wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()
text = "Your answer wasn't correct, please try again."
searhed_word = (text).lower()
actual_word = wait.until(EC.visibility_of_element_located(TEXT_AFTER_SUBMIT_BTN)).text.lower()
print(f'Text actual: "{actual_word}" VS text expected: "{searhed_word}"')
if searhed_word in actual_word:
    print(f'Text is OK: "{searhed_word}"\n')
else:
    print(f'Text actual: "{actual_word}"\n')
assert searhed_word in actual_word

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()


