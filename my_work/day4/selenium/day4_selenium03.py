from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')

input_element = driver.find_element_by_name('query')
input_element.send_keys('Python')
input_element.send_keys(Keys.ENTER)

from bs4 import BeautifulSoup as BS

html = driver.page_source
bsObj = BS(html, 'html.parser')

ul_tag = bsObj.find('ul', {'class':'lst_type'})

lis = ul_tag.find_all('li')

for li in lis:
    a_tag = li.find('a')
    print('text:{}   link:{}'.format(a_tag.text, a_tag['href']))