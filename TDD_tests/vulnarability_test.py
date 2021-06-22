from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screenshot import Screenshot_Clipping
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
URL_FLD = (By.XPATH, "//input[@inputmode='search']")
SRCH_BTN = (By.XPATH, "//button[@class='button search__btn button--color-blue button--v-default button--size-lg']")
SCRT_SCR = (By.XPATH, "(//span[@class='security-level__score'])[2]")
CRTCL_RSK = (By.XPATH, "(//div[@class='severity__count'])[1]")
MDM_RSK = (By.XPATH, "(//div[@class='severity__count'])[2]")
ELVT_RSK = (By.XPATH, "(//div[@class='severity__count'])[3]")
ISSR_DN = (By.XPATH, "//pre[@class='pre-text']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://spyse.com/' )

# 2. Send https://www.autocareparts.com/ to field
url_t_tst = 'https://www.autocareparts.com/'
wait.until(EC.presence_of_element_located(URL_FLD)).clear()
wait.until(EC.presence_of_element_located(URL_FLD)).send_keys(url_t_tst)

# 3. Click on Search button
wait.until(EC.element_to_be_clickable(SRCH_BTN)).click()

# 4. Find security score, critical risk, medium risk, elevated risk, issuer DN
security_score = wait.until(EC.visibility_of_element_located(SCRT_SCR)).text.lower()
critical_risk = wait.until(EC.visibility_of_element_located(CRTCL_RSK)).text.lower()
medium_risk = wait.until(EC.visibility_of_element_located(MDM_RSK)).text.lower()
elevated_risk = wait.until(EC.visibility_of_element_located(ELVT_RSK)).text.lower()
issuer_dn = wait.until(EC.visibility_of_element_located(ISSR_DN)).text.lower()
print(f'Security score: "{security_score}";\nCritical risk: "{critical_risk}";\nMedium risk: "{medium_risk}"\n'
      f'Elevated risk: "{elevated_risk}";\nIssuer DN: "{issuer_dn}"')

# 5. Make a screenshot of the whole page
ob=Screenshot_Clipping.Screenshot()
url = driver.current_url
today = time.strftime(f'%Y_%m_%d')
now = time.strftime(f'%H_%M_%S')
file_name = 'vulnarability_' + today + '_' + now + '.jpg'
img_url=ob.full_Screenshot(driver, save_path=r'C:\Everything\IT\Testing\Automation_08_09_2019\autocareparts_gene_kayakov\screen_shots', image_name= file_name)
print(img_url)

driver.close()

# Sleep to see what we have
sleep(4)

# Driver quit
driver.quit()


