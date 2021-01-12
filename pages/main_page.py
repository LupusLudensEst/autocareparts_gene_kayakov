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
        expected_text = '310.817.0370'
        actual_text = wait.until(EC.visibility_of_element_located((PHONE_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 4 Verify address "20350 NE 16TH PL" is here
    def vrf_addrss_here(self, phone):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(CONTACT_US))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        expected_text = '20350 NE 16TH PL'
        actual_text = wait.until(EC.visibility_of_element_located((ADDRESS_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code

    # 5 Verify email "sales@autocareparts.com" is here
    def vrf_eml_here(self, phone):
        wait = WebDriverWait(self.driver, 10)
        target = wait.until(EC.element_to_be_clickable(CONTACT_US))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()
        sleep(1.5)
        expected_text = 'sales@autocareparts.com'
        actual_text = wait.until(EC.visibility_of_element_located((EMAIL_IS_HERE))).text
        print(f'Actual phone: {actual_text}')
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    # End of the above code














