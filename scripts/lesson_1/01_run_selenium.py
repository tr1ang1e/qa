from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By  # class for define element search method

# specify options (is not used currently)
options = webdriver.ChromeOptions()
options.add_argument("")

# initialize driver  >>  browser window must appear
driver = webdriver.Chrome(chrome_options=options)
sleep(5)

#   [ in] = web-address 
driver.get("https://stepik.org/lesson/25969/step/12")
sleep(5)

# find element on web page
#   [ in] = search method 
#   [ in] = search key
#   [out] = found element
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
sleep(5)

# find and press button
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()
sleep(5)

# destroy session
driver.quit()



