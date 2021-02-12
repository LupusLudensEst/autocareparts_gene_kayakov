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
SHOP_BY_BRANDS = (By.XPATH, "(//a[@class='site-nav--link'])[2]")
SHOP_BY_BRANDS_BY_MENU = (By.XPATH, "//span[@class='icon icon-arrow-down']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Hover over Shop By Brand
target = wait.until(EC.visibility_of_element_located(SHOP_BY_BRANDS))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.perform()

# 3. Verify that Shop By Brand has 9 elements
expected_quantity = 9
quantity_elements = len(driver.find_elements(*SHOP_BY_BRANDS_BY_MENU))
if expected_quantity == quantity_elements:
    print(f'Ok, we have: {quantity_elements} elements')
else:
    print(f'Not ok, we have: {quantity_elements} elements')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()