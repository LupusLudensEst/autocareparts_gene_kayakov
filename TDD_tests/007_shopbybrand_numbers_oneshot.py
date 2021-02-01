from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
SHOP_BY_BRAND = (By.XPATH, "(//a[@class='site-nav--link'])[2]")
NUMBERS = (By.XPATH, "(//a[@class='site-nav--link'])[3]")
ONE_SHOT = (By.XPATH, "(//a[@class='site-nav--link'])[4]")
ONESHOT_TEXT_HERE = (By.XPATH, "//h1[@class='section-header--title h1']")

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
# 4. Click on One shot button
driver.find_element(*ONE_SHOT).click()
# 6. Verify searched word in Shop by Brand, Numbers, 1 Shot "1 SHOT" is here
searhed_word = ('1 SHOT').lower()
actual_text = (driver.find_element( *ONESHOT_TEXT_HERE ).text).lower()
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