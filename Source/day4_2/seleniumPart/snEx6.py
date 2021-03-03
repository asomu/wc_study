from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(1)
driver.get('http://www.danawa.com')
time.sleep(3)

def mouseOverElement(title):
    element = driver.find_elements_by_link_text(title)[0]
    ActionChains(driver).move_to_element(element).perform()
    return element

mouseOverElement('가전/TV')
mouseOverElement('TV')
mouseOverElement('올레드 TV')
mouseOverElement('8K 올레드 TV').click()

