from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://www.google.com')
