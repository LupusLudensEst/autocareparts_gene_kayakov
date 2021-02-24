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
CART_BTN = (By.XPATH, "//a[@class='header-cart-btn cart-toggle']")
CART_EMPTHY_TEXT = (By.XPATH, "//*[@id='ajaxifyCart']/h2")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Click on Cart button
target = wait.until(EC.visibility_of_element_located(CART_BTN))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()

# 3. Verify text "YOUR CART IS CURRENTLY EMPTY." is here
text = 'YOUR CART IS CURRENTLY EMPTY.'
searhed_word = text.lower()
actual_word = wait.until(EC.presence_of_element_located(CART_EMPTHY_TEXT)).text.lower()
print(f'Word actual: "{actual_word}" VS word expected: "{searhed_word}"')
assert searhed_word in actual_word
if searhed_word in actual_word:
    print(f'Expected word is OK: "{searhed_word}"\n')
else:
    print(f'Actual word: "{actual_word}"\n')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()