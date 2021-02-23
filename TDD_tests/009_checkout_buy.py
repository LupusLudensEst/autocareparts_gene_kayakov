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
CARPRO = (By.XPATH, "(//a[@class='featured-box'])[1]")
CARPRO_CQUARZ_FABRIC = (By.XPATH, "(//div[@class='lazyload__image-wrapper no-js'])[1]")
ADD_TO_CART = (By.ID, "addToCartText-product-template")
CHECK_OUT = (By.XPATH, "(//span[@class='icon icon-cart'])[4]")
EMAIL_OR_MOBILE = (By.ID, "checkout_email_or_phone")
FIRST_NAME_CHECKOUT = (By.ID, "checkout_shipping_address_first_name")
LAST_NAME_CHECKOUT = (By.ID, "checkout_shipping_address_last_name")
ADDRESS = (By.ID, "checkout_shipping_address_address1")
CITY = (By.ID, "checkout_shipping_address_city")
COUNTRY = (By.XPATH, "//select[@id='checkout_shipping_address_country']")
STATE = (By.XPATH, "//select[@id='checkout_shipping_address_province']")
ZIP = (By.ID, "checkout_shipping_address_zip")
CONTINUE_TO_SHIPPING = (By.ID, "continue_button")
CONTACT_TEXT = (By.XPATH, "(//div[@class='review-block__content'])[1]")
SHIP_TO_TEXT = (By.XPATH, "(//div[@class='review-block__content'])[2]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Click on Carpro
wait.until(EC.element_to_be_clickable(CARPRO)).click()
# 3. Click on CarPro Cquartz Fabric #1117n, 500 ml
wait.until(EC.element_to_be_clickable(CARPRO_CQUARZ_FABRIC)).click()
# 4. Click on Add to Cart
wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
# 5. Click on CHECK_OUT
wait.until(EC.element_to_be_clickable(CHECK_OUT)).click()
# 6. Enter Email or mobile phone number
password = str(randint(1000000000, 9999999999))
name = 'name' + '_' + password
last_name = ''.join(reversed(name))
email = (name + '@sample.com')
print(f'\nName: {name}, last name: {last_name}, password: {password} and email: {email}\n')
wait.until(EC.presence_of_element_located(EMAIL_OR_MOBILE)).clear()
wait.until(EC.presence_of_element_located(EMAIL_OR_MOBILE)).send_keys(email)
# 7. Enter FIRST_NAME
wait.until(EC.presence_of_element_located(FIRST_NAME_CHECKOUT)).clear()
wait.until(EC.presence_of_element_located(FIRST_NAME_CHECKOUT)).send_keys(name)
# 8. Enter LAST_NAME
wait.until(EC.presence_of_element_located(LAST_NAME_CHECKOUT)).clear()
wait.until(EC.presence_of_element_located(LAST_NAME_CHECKOUT)).send_keys(last_name)
# 9. Enter ADDRESS
address = '2124 NE 182nd St North Miami Beach, Fl 33162'
wait.until(EC.presence_of_element_located(ADDRESS)).clear()
wait.until(EC.presence_of_element_located(ADDRESS)).send_keys(address)
# 10. Enter CITY
wait.until(EC.presence_of_element_located(CITY)).clear()
wait.until(EC.presence_of_element_located(CITY)).send_keys('North Miami Beach')
# 11. Enter COUNTRY
# wait.until(EC.presence_of_element_located(COUNTRY)).clear()
wait.until(EC.presence_of_element_located(COUNTRY)).send_keys('United States')
# 12. Enter STATE
wait.until(EC.element_to_be_clickable(STATE)).send_keys('Florida')
# 13. Enter ZIP
wait.until(EC.presence_of_element_located(ZIP)).clear()
wait.until(EC.presence_of_element_located(ZIP)).send_keys('33162')
# 14. Click on Continue to shipping
target = wait.until(EC.element_to_be_clickable(CONTINUE_TO_SHIPPING))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click(on_element = target)
actions.perform()
# 15. Verify Contact=email text is here
searhed_email = (email).lower()
actual_email = (wait.until(EC.presence_of_element_located(CONTACT_TEXT)).text).lower()
print(f'Email actual: "{actual_email}" VS email expected: "{searhed_email}"')
assert searhed_email in actual_email
if searhed_email in actual_email:
    print(f'Expected email is OK: "{searhed_email}"\n')
else:
    print(f'Actual email: "{actual_email}"\n')
# 16. Verify Ship to=address text is here
searhed_address = (address).lower()
actual_address = (driver.find_element( *SHIP_TO_TEXT ).text).lower()
print(f'Actual address: "{actual_address}" VS expected address: "{searhed_address}"')
assert searhed_address in actual_address
if searhed_address in actual_address:
    print(f'Expected address is OK: "{searhed_address}"')
else:
    print(f'Actual address: "{actual_address}"')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()