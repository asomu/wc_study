from selenium import webdriver
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus

driver = webdriver.Chrome('../../day4/selenium/chromedriver.exe')
keyword = quote_plus('무선청소기')
total_page = 10
prod_data_total = []

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title=''
        try:
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list=''
        try:
            price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
        except:
            price=''
        prod_data.append([title, spec_list, price])
    return prod_data

def get_search_page_url(keyword, page):
    return 'http://search.danawa.com/dsearch.php?query={}&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&tab=goods'.format(keyword, page)

for page in range(1,total_page+1):
    url = get_search_page_url(keyword, page)
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
    prod_item_list = get_prod_items(prod_items)
    prod_data_total  = prod_data_total + prod_item_list

print(prod_data_total)

import pandas as pd

data = pd.DataFrame(prod_data_total, columns=['title','spec','price'])
data.to_csv('./../files/danawa_crawling_result2.csv', index=False , encoding='utf-8')
