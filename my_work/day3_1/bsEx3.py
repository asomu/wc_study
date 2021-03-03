from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


url = "https://finance.naver.com/"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser', from_encoding='ms949')

news_area = bs.find('div', {'class':'section_strategy'})

lis = news_area.find_all('li')
for li in lis:
    atag = li.find('a')
    print(atag.text)


