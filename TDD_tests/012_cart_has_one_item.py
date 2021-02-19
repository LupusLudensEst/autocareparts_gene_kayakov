from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
SHOP_BY_BRAND = (By.XPATH, "(//a[@class='site-nav--link'])[2]")
NUMBERS = (By.XPATH, "(//a[@class='site-nav--link'])[3]")
ONE_SHOT = (By.XPATH, "(//a[@class='site-nav--link'])[4]")
ONESHOT_TEXT_HERE = (By.XPATH, "//h1[@class='section-header--title h1']")
ONE_SHOT_PIC = (By.XPATH, "//div[@class='product-grid-image']")
ADD_TO_CART = (By.XPATH, "//span[@id='addToCartText-product-template']")
CLOSE_SHOPPING_CART = (By.XPATH, "//button[@title='Close Cart']")
QUANTITY_IN_CART = (By.XPATH, "//span[@class='cart-count cart-badge--desktop']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# Activate ActionChains
action = ActionChains(driver)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Hover over Shop by Brand button
action.move_to_element(driver.find_element(*SHOP_BY_BRAND)).perform()
# 3. Hover over Numbers button
action.move_to_element(driver.find_element(*NUMBERS)).perform()
# 4. Hover over One shot button
action.move_to_element(driver.find_element(*ONE_SHOT)).perform()
# 5. Click on One shot button
driver.find_element(*ONE_SHOT).click()
# 6. Click on One shot picture
target = wait.until(EC.element_to_be_clickable(ONE_SHOT_PIC))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()
# 7. Click on Add to Cart button
driver.find_element(*ADD_TO_CART).click()
# 8. Click and close shopping cart
target = wait.until(EC.element_to_be_clickable(CLOSE_SHOPPING_CART))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()
# 9. Verify "1" is in the cart
text = '1'
searhed_word = (text).lower()
actual_word = (wait.until(EC.presence_of_element_located(QUANTITY_IN_CART)).text).lower()
print(f'Quantity actual: "{actual_word}" VS quantity expected: "{searhed_word}"')
if searhed_word in actual_word:
    print(f'Expected quantity is OK: "{searhed_word}"\n')
else:
    print(f'Actual quantity: "{actual_word}"\n')
assert searhed_word in actual_word

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()