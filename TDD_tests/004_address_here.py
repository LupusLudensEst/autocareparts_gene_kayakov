from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
CONTACT_US = (By.XPATH, "//a[@href='/pages/contact-us']")
ADDRESS_IS_HERE = (By.XPATH, "//div[@class='rte']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Verify address "20350 NE 16TH PL" is here
target = wait.until(EC.element_to_be_clickable(CONTACT_US))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()
sleep(1.5)
expected_text = '20350 NE 16TH PL'
actual_text = wait.until(EC.visibility_of_element_located((ADDRESS_IS_HERE))).text
print(f'Actual phone: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
