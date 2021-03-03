from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com"
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser', from_encoding='ms949')

news_txarea = bsObj.find('div',{'class':'section_strategy'})
print(news_txarea)

lis = news_txarea.findAll('li')
for li in lis:
    atag = li.find('a')
    print(atag.text)

