from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
CREATE_AN_ACCOUNT = (By.XPATH, "(//a[@id='customer_register_link'])[1]")
FIRST_NAME = (By.ID, "first_name")
LAST_NAME = (By.ID, "last_name")
EMAIL = (By.ID, "email")
PASSWORD = (By.ID, "create_password")
I_AM_NOT_ROBOT_CHCK_BX = (By.XPATH, "//div[@class='recaptcha-checkbox-checkmark']")
CREATE_BTN = (By.XPATH, "//input[@class='btn']")
SKIP_CAPCHA = (By.ID, "recaptcha-verify-button")
SELECT_TEXT_HERE = (By.XPATH, "//div[@class='rc-imageselect-desc-no-canonical']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Click on Create an Account button
wait.until(EC.element_to_be_clickable(CREATE_AN_ACCOUNT)).click()

# 3. Send First Name
wait.until(EC.presence_of_element_located(FIRST_NAME)).clear()
wait.until(EC.presence_of_element_located(FIRST_NAME)).send_keys('American')
# 4. Send Last Name
wait.until(EC.presence_of_element_located(LAST_NAME)).clear()
wait.until(EC.presence_of_element_located(LAST_NAME)).send_keys('Psycho')
# 5. Send Email
wait.until(EC.presence_of_element_located(EMAIL)).clear()
wait.until(EC.presence_of_element_located(EMAIL)).send_keys('psycho@psycho.org')
# 6. Send Password
password = str(randint(1000000000, 9999999999))
wait.until(EC.presence_of_element_located(PASSWORD)).clear()
wait.until(EC.presence_of_element_located(PASSWORD)).send_keys(password)
# 7. Click Create button
wait.until(EC.element_to_be_clickable(CREATE_BTN)).click()
# 8. Mark checkbox "I am not a robot"
seq = driver.find_elements_by_tag_name('iframe')
print(f'Iframes: {seq}')
print(f'Iframes: {len(seq)}')
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.frame(iframe)
target = wait.until(EC.element_to_be_clickable(I_AM_NOT_ROBOT_CHCK_BX))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click(on_element = target)
actions.perform()
driver.switch_to.default_content()
# 9. Click Skip captcha button
seq = driver.find_elements_by_tag_name('iframe')
print(f'Iframes: {seq}')
print(f'Iframes: {len(seq)}')
iframe = driver.find_elements_by_tag_name('iframe')[3]
driver.switch_to.frame(iframe)
wait.until(EC.element_to_be_clickable(SKIP_CAPCHA)).click()
# 10. Verify "Select all images with" text is here
searhed_word = ('Select').lower()
actual_text = (driver.find_element( *SELECT_TEXT_HERE ).text).lower()
print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}" ')
assert searhed_word in actual_text
if searhed_word in actual_text:
    print(f'Text is here: "{searhed_word}"')
else:
    print(f'Actual text is here: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
