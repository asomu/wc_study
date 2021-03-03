import dload
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time

searchStr = input('찾을 이미지 이름: ')

baseUrl = 'https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q='
url = baseUrl + quote_plus(searchStr)


driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(5)

html = driver.page_source
bsObj = BS(html, 'html.parser')

thumbnails = bsObj.select('#imgList > div > a > img')

for i, thumbnail in enumerate(thumbnails):
    src = thumbnail['src']
    dload.save(src, f'imgs/{i}.jpg')

driver.quit()