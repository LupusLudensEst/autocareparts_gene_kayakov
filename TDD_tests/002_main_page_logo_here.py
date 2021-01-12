from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGO_IS_HERE = (By.XPATH, "//img[@srcset='//cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_180x.png?v=1591034175 180w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_360x.png?v=1591034175 360w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_540x.png?v=1591034175 540w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_720x.png?v=1591034175 720w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_900x.png?v=1591034175 900w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1080x.png?v=1591034175 1080w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1296x.png?v=1591034175 1296w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1512x.png?v=1591034175 1512w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_1728x.png?v=1591034175 1728w, //cdn.shopify.com/s/files/1/0742/6707/files/autocareparts-website-logo2_4b14c722-a146-4324-a06a-df573049679e_2048x.png?v=1591034175 2048w']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://www.autocareparts.com/' )

# 2. Verify logo "Auto Care Parts" is here
if wait.until(EC.visibility_of_element_located((LOGO_IS_HERE))) :
    print("Image is displayed")
else :
    print("image is not displayed")

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
