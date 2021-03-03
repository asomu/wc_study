from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.request

url = "https://www.naver.com/"

html = urlopen(url)
bs4 = bs(html, 'html.parser')

service_area = bs4.find('img')
print(service_area['src'])
urllib.request.urlretrieve(service_area['src'], service_area['src'][-1])
