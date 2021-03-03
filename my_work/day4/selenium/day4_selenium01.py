from selenium import webdriver

URL = "https://nid.naver.com/nidlogin.login"

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
driver.get(URL)

driver.find_element_by_name('id').send_keys('asomu')
driver.find_element_by_name('pw').send_keys('Judith6846.')
driver.find_element_by_xpath('//*[@id="log.login"]').click()