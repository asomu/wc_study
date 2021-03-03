from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.naver.com/'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')
#print(bsObj)

start_page = bsObj.find('div',{'class':'service_area'})
#print(start_page)

first_atag = start_page.find('a')
print(first_atag)
print(first_atag.text)
print(first_atag['href'])
