from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
VISA_TEXT_HERE = (By.ID, "pi-visa")
AMEX_TEXT_HERE = (By.ID, "pi-american_express")
APPLE_PAY_TEXT_HERE = (By.ID, "pi-apple_pay")
DINERS_CLUB_TEXT_HERE = (By.ID, "pi-diners_club")
DISCOVER_TEXT_HERE = (By.ID, "pi-discover")
ELO_TEXT_HERE = (By.ID, "pi-elo")
GOOGLE_PAY_TEXT_HERE = (By.ID, "pi-google_pay")
JCB_TEXT_HERE = (By.ID, "pi-jcb")
MASTER_CARD_TEXT_HERE = (By.ID, "pi-master")
SHOPIFY_PAY_TEXT_HERE = (By.ID, "pi-shopify_pay")

# Explicit wait
wait = WebDriverWait(driver, 15)

# Activate ActionChains
action = ActionChains(driver)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

def verify_text(expected_text, locator):
    actual_text = driver.find_element(*locator).text
    assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'
    print(f'Expected text: {expected_text} VS actual text: {actual_text}')

# 2. Verify Amex text is here
am_ex_text = "American Express"
verify_text(am_ex_text, AMEX_TEXT_HERE)

# 3. Verify Apple Pay text is here
app_pay_text = "Apple Pay"
verify_text(app_pay_text, APPLE_PAY_TEXT_HERE)

# 4. Verify Diners Club text is here
din_cl_text = "Diners Club"
verify_text(din_cl_text, DINERS_CLUB_TEXT_HERE)

# 5. Verify Discover text is here
discov_text = "Discover"
verify_text(discov_text, DISCOVER_TEXT_HERE)

# 6. Verify Elo text is here
elo_text = "Elo"
verify_text(elo_text, ELO_TEXT_HERE)

# 7. Verify Google Pay text is here
goo_pay_text = "Google Pay"
verify_text(goo_pay_text, GOOGLE_PAY_TEXT_HERE)

# 8. Verify JCB text is here
jcb_text = "JCB"
verify_text(jcb_text, JCB_TEXT_HERE)

# 9. Verify Mastercard text is here
ms_crd_text = "Mastercard"
verify_text(ms_crd_text, MASTER_CARD_TEXT_HERE)

# 10. Verify Shop Pay text is here
shop_pay_text = "Shop Pay"
verify_text(shop_pay_text, SHOPIFY_PAY_TEXT_HERE)

# 11. Verify Visa text is here
visa_text = "Visa"
verify_text(visa_text, VISA_TEXT_HERE)

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
