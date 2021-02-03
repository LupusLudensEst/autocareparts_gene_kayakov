from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Locators
TEXT_IS_HERE = (By.XPATH, "//div[@class='grid-item large--two-fifths']")
LOGO_IS_HERE = (By.XPATH, "//img[@srcset='//cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_180x.png?v=1591034175 180w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_360x.png?v=1591034175 360w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_540x.png?v=1591034175 540w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_720x.png?v=1591034175 720w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_900x.png?v=1591034175 900w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1080x.png?v=1591034175 1080w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1296x.png?v=1591034175 1296w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1512x.png?v=1591034175 1512w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1728x.png?v=1591034175 1728w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_2048x.png?v=1591034175 2048w']")
CONTACT_US = (By.XPATH, "//a[@href='/pages/contact-us']")
PHONE_IS_HERE = (By.XPATH, "//div[@class='rte']")
ADDRESS_IS_HERE = (By.XPATH, "//div[@class='rte']")
EMAIL_IS_HERE = (By.XPATH, "//div[@class='rte']")
SEARCH_FIELD = (By.NAME, "q")
SEARCHED_IS_HERE = (By.XPATH, "//h1[@class='h2 text-center']")
SEARCH_BTN = (By.XPATH, "(//span[@class='icon icon-search'])[1]")
SHOP_BY_BRAND = (By.XPATH, "(//a[@class='site-nav--link'])[2]")
NUMBERS = (By.XPATH, "(//a[@class='site-nav--link'])[3]")
ONE_SHOT = (By.XPATH, "(//a[@class='site-nav--link'])[4]")
ONESHOT_TEXT_HERE = (By.XPATH, "//h1[@class='section-header--title h1']")
CREATE_AN_ACCOUNT = (By.XPATH, "(//a[@id='customer_register_link'])[1]")
FIRST_NAME = (By.ID, "first_name")
LAST_NAME = (By.ID, "last_name")
EMAIL = (By.ID, "email")
PASSWORD = (By.ID, "create_password")
I_AM_NOT_ROBOT_CHCK_BX = (By.XPATH, "//div[@class='recaptcha-checkbox-checkmark']")
CREATE_BTN = (By.XPATH, "//input[@class='btn']")
SKIP_CAPCHA = (By.ID, "recaptcha-verify-button")
SELECT_TEXT_HERE = (By.XPATH, "//div[@class='rc-imageselect-desc-no-canonical']")
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

class MainPage(Page):

    # 1 Verify text "© 2021 AutoCareParts.com Powered by Shopify" is here
    def vrfy_txt_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = '© 2021 AutoCareParts.com Powered by Shopify'
        sleep(1.5)
        actual_text = wait.until(EC.presence_of_element_located((TEXT_IS_HERE))).text
        print(f'Actual text: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 2 Verify logo "Auto Care Parts" is here
    def vrf_logo_here(self):
        wait = WebDriverWait(self.driver, 10)
        if wait.until(EC.visibility_of_element_located((LOGO_IS_HERE))):
            print("Image is displayed")
        else:
            print("image is not displayed")

    # End of the above code

    # 3 Verify phone "310.817.0370" is here
    def vrf_phn_here(self, phone):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(CONTACT_US))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        expected_text = phone
        actual_text = wait.until(EC.visibility_of_element_located((PHONE_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 4 Verify address "20350 NE 16TH PL" is here
    def vrf_addrss_here(self, addrss):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(CONTACT_US))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        expected_text = addrss
        actual_text = wait.until(EC.visibility_of_element_located((ADDRESS_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 5 Verify email "sales@autocareparts.com" is here
    def vrf_eml_here(self, eml):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(CONTACT_US))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        expected_text = eml
        actual_text = wait.until(EC.visibility_of_element_located((EMAIL_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 6 Verify searched word  is here
    def vrf_srchwrd_here(self,txt):
        wait = WebDriverWait(self.driver, 10)
        # Send search word to the search field
        searhed_word = txt.lower()
        e = self.driver.find_element(*SEARCH_FIELD)
        e.clear()
        e.send_keys(searhed_word)
        sleep(4)
        # Click on search button
        self.driver.find_element(*SEARCH_BTN).click()
        # Verify searched word is here
        actual_text = (self.driver.find_element(*SEARCHED_IS_HERE).text).lower()
        print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}" ')
        assert searhed_word in actual_text
        if searhed_word in actual_text:
            print(f'Text is here: "{searhed_word}"')
        else:
            print(f'Actual text is here: "{actual_text}" ')

    # End of the above code

    # 7 Verify searched word "1 SHOT" is here
    def shopbybrand_numbers_oneshot(self, txt):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)
        # Hover over Shop by Brand button
        actions.move_to_element(self.driver.find_element(*SHOP_BY_BRAND)).perform()
        # Hover over Numbers button
        actions.move_to_element(self.driver.find_element(*NUMBERS)).perform()
        # Hover over One shot button
        actions.move_to_element(self.driver.find_element(*ONE_SHOT)).perform()
        # Click on One shot button
        self.driver.find_element(*ONE_SHOT).click()
        # Verify searched word "1 SHOT" is here
        searhed_word = (txt).lower()
        actual_text = (self.driver.find_element(*ONESHOT_TEXT_HERE).text).lower()
        print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}"')
        assert searhed_word in actual_text
        if searhed_word in actual_text:
            print(f'Text is here: "{searhed_word}" ')
        else:
            print(f'Actual text is here: "{actual_text}" ')

    # End of the above code

    # 8 Verify searched word "1 SHOT" is here
    def captcha_works(self, txt):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)
        # Click on Create an Account button
        wait.until(EC.element_to_be_clickable(CREATE_AN_ACCOUNT)).click()
        # Send First Name
        wait.until(EC.presence_of_element_located(FIRST_NAME)).clear()
        wait.until(EC.presence_of_element_located(FIRST_NAME)).send_keys('American')
        # Send Last Name
        wait.until(EC.presence_of_element_located(LAST_NAME)).clear()
        wait.until(EC.presence_of_element_located(LAST_NAME)).send_keys('Psycho')
        # Send Email
        wait.until(EC.presence_of_element_located(EMAIL)).clear()
        wait.until(EC.presence_of_element_located(EMAIL)).send_keys('psycho@psycho.org')
        # Send Password
        password = str(randint(1000000000, 9999999999))
        wait.until(EC.presence_of_element_located(PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(PASSWORD)).send_keys(password)
        # Click Create button
        wait.until(EC.element_to_be_clickable(CREATE_BTN)).click()
        # Mark checkbox "I am not a robot"
        seq = self.driver.find_elements_by_tag_name('iframe')
        print(f'Iframes: {seq}')
        print(f'Iframes: {len(seq)}')
        iframe = self.driver.find_elements_by_tag_name('iframe')[0]
        self.driver.switch_to.frame(iframe)
        target = wait.until(EC.element_to_be_clickable(I_AM_NOT_ROBOT_CHCK_BX))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(on_element=target)
        actions.perform()
        self.driver.switch_to.default_content()
        # Click Skip captcha button
        seq = self.driver.find_elements_by_tag_name('iframe')
        print(f'Iframes: {seq}')
        print(f'Iframes: {len(seq)}')
        iframe = self.driver.find_elements_by_tag_name('iframe')[3]
        self.driver.switch_to.frame(iframe)
        wait.until(EC.element_to_be_clickable(SKIP_CAPCHA)).click()
        # 10. Verify "Select all images with" text is here
        searhed_word = ('Select').lower()
        actual_text = (self.driver.find_element(*SELECT_TEXT_HERE).text).lower()
        print(f'Actual text: "{actual_text}" VS Expected text: "{searhed_word}" ')
        assert searhed_word in actual_text
        if searhed_word in actual_text:
            print(f'Text is here: "{searhed_word}"')
        else:
            print(f'Actual text is here: "{actual_text}" ')


    # End of the above code

    # 8 Verify Contact=email(randomized) and Ship to=address '2124 NE 182nd St North Miami Beach, Fl 33162' are here
    def contact_and_address_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)
        # Click on Carpro
        wait.until(EC.element_to_be_clickable(CARPRO)).click()
        # Click on CarPro Cquartz Fabric #1117n, 500 ml
        wait.until(EC.element_to_be_clickable(CARPRO_CQUARZ_FABRIC)).click()
        # Click on Add to Cart
        wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
        # Click on CHECK_OUT
        wait.until(EC.element_to_be_clickable(CHECK_OUT)).click()
        # Enter Email or mobile phone number
        password = str(randint(1000000000, 9999999999))
        name = 'name' + password
        last_name = ''.join(reversed(name))
        email = (name + '@sample.com')
        print(f'\nName: {name}, last name: {last_name}, password: {password} and email: {email}\n')
        wait.until(EC.presence_of_element_located(EMAIL_OR_MOBILE)).clear()
        wait.until(EC.presence_of_element_located(EMAIL_OR_MOBILE)).send_keys(email)
        # Enter FIRST_NAME
        wait.until(EC.presence_of_element_located(FIRST_NAME_CHECKOUT)).clear()
        wait.until(EC.presence_of_element_located(FIRST_NAME_CHECKOUT)).send_keys(name)
        # Enter LAST_NAME
        wait.until(EC.presence_of_element_located(LAST_NAME_CHECKOUT)).clear()
        wait.until(EC.presence_of_element_located(LAST_NAME_CHECKOUT)).send_keys(last_name)
        # Enter ADDRESS
        address = '2124 NE 182nd St North Miami Beach, Fl 33162'
        wait.until(EC.presence_of_element_located(ADDRESS)).clear()
        wait.until(EC.presence_of_element_located(ADDRESS)).send_keys(address)
        # Enter CITY
        wait.until(EC.presence_of_element_located(CITY)).clear()
        wait.until(EC.presence_of_element_located(CITY)).send_keys('North Miami Beach')
        # Enter COUNTRY
        # wait.until(EC.presence_of_element_located(COUNTRY)).clear()
        wait.until(EC.presence_of_element_located(COUNTRY)).send_keys('United States')
        # Enter STATE
        wait.until(EC.element_to_be_clickable(STATE)).send_keys('Florida')
        # Enter ZIP
        wait.until(EC.presence_of_element_located(ZIP)).clear()
        wait.until(EC.presence_of_element_located(ZIP)).send_keys('33162')
        # Click on Continue to shipping
        target = wait.until(EC.element_to_be_clickable(CONTINUE_TO_SHIPPING))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(on_element=target)
        actions.perform()
        # Verify Contact=email text is here
        searhed_email = (email).lower()
        actual_email = (self.driver.find_element(*CONTACT_TEXT).text).lower()
        print(f'Email actual: "{actual_email}" VS email expected: "{searhed_email}"')
        assert searhed_email in actual_email
        if searhed_email in actual_email:
            print(f'Expected email is OK: "{searhed_email}"\n')
        else:
            print(f'Actual email: "{actual_email}"\n')
        # Verify Ship to=address text is here
        searhed_address = (address).lower()
        actual_address = (self.driver.find_element(*SHIP_TO_TEXT).text).lower()
        print(f'Actual address: "{actual_address}" VS expected address: "{searhed_address}"')
        assert searhed_address in actual_address
        if searhed_address in actual_address:
            print(f'Expected address is OK: "{searhed_address}"')
        else:
            print(f'Actual address: "{actual_address}"')

    # End of the above code














