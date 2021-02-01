from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
SEARCH_FIELD = (By.NAME, "q")
SEARCHED_IS_HERE = (By.XPATH, "//h1[@class='h2 text-center']")
SEARCH_BTN = (By.XPATH, "(//span[@class='icon icon-search'])[1]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Send search word to the search field
searhed_word = ('gorilla').lower()
e = driver.find_element( *SEARCH_FIELD )
e.clear()
e.send_keys(searhed_word)
sleep(4)

# 3. Click on search button
driver.find_element( *SEARCH_BTN ).click()

# 4. Verify searched word "gorilla" is here
actual_text = (driver.find_element( *SEARCHED_IS_HERE ).text).lower()
print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}"')
assert searhed_word in actual_text
if searhed_word in actual_text:
    print(f'Text is here: "{searhed_word}" ')
else:
    print(f'Actual text is here: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()