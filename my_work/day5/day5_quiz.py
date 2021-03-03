from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

URL = "http://www.jolse.com/"

driver = webdriver.Chrome('chromedriver.exe')
driver.get(URL)


def get_search_page_url(current_url, page):
    url = f"{current_url}?page={page}"
    print(url)
    return url


def mouse_over_element(title):
    element = driver.find_elements_by_link_text(title)[0]
    ActionChains(driver).move_to_element(element).perform()
    return element


def get_page_html(url):
    driver.get(url)
    time.sleep(1)
    page_html = driver.page_source
    return page_html


def get_item_info(html):
    bsObj = BeautifulSoup(html, 'html.parser')
    items = bsObj.select('ul.prdList > li.item')
    for item in items:
        name = item.select('ul.prdList > li.item > div.box > div.description > div.fadearea > p.name > a._evt_tracker0 > span')[0].text.strip()
        name_list.append(name)
        price = item.select('ul.prdList > li.item > div.box > div.description > div.fadearea > ul.xans-product > li.xans-record- > span')[0].text.strip()
        price_list.append(price)
        product_list.append([name, price])


mouse_over_element('SKINCARE')
time.sleep(2)
mouse_over_element('Moisturizers')
time.sleep(2)
mouse_over_element('Toners & Mists').click()
time.sleep(2)

current_url = driver.current_url
print(current_url)

product_list = []
name_list = []
price_list = []


get_item_info(get_page_html(current_url))
for page in range(2,6):
    page_html = get_page_html(get_search_page_url(current_url, page))
    get_item_info(page_html)

#for i, item in enumerate(name_list):
#    print(f"{name_list[i]}, {price_list[i]}")

for item in product_list:
    print(item)

import os
import pandas as pd
data = pd.DataFrame(product_list, columns=['상품명','가격'])

if os.path.isdir('./files/'):
    data.to_csv('./files/jolse_pruduct_list.csv', index=False)
else:
    os.mkdir('./files/')
    data.to_csv('./files/jolse_pruduct_list.csv', index=False)


