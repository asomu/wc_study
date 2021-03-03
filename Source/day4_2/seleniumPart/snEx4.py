from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naver.com')

input_element = driver.find_element_by_name('query')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

from bs4 import BeautifulSoup

html = driver.page_source
bsObj = BeautifulSoup(html,'html.parser')

ul_tag = bsObj.find('ul', {'class':'lst_type'})
#print(ul_tag)

lis = ul_tag.findAll('li')

for li in lis:
    a_tag = li.find('a')
    print('text:{}   link:{}'.format(a_tag.text, a_tag['href']))

print()

tag = bsObj.select('ul>li>a')
print(tag)
