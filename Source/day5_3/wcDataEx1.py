from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
url = 'http://search.danawa.com/dsearch.php?query=무선청소기&tab=main'
driver.get(url)

time.sleep(3)
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

prod_items = soup.select('div.main_prodlist > ul.product_list > li.prod_item')
#print(prod_items)
#print(len(prod_items))

title = prod_items[0].select('p.prod_name > a')[0].text.strip()
print(title)

spec_list = prod_items[0].select('div.spec_list')[0].text.strip()
print(spec_list)

price = prod_items[0].select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
print(price)

def get_prod_items(prod_items):
    prod_data = []
    for prod_item in prod_items:
        try:
            title = prod_item.select('p.prod_name > a')[0].text.strip()
        except:
            title = ''
        try:
            spec_list = prod_item.select('div.spec_list')[0].text.strip()
        except:
            spec_list = ''
        try:
            price = prod_item.select('li.rank_one > p.price_sect > a > strong')[0].text.strip().replace(',','')
        except:
            price = ''
        prod_data.append([title, spec_list, price])
    return prod_data

prod_data = get_prod_items(prod_items)
print(prod_data)

def get_search_page_url(keyword, page):
    return 'http://search.danawa.com/dsearch.php?query={}&volumeType=allvs&page={}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&tab=goods'.format(keyword, page)

from urllib.parse import quote_plus
keyword = quote_plus('무선청소기')
page = 1
url = get_search_page_url(keyword, page)
print(url)
