from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')

bsObj = BeautifulSoup(html, 'html.parser')

for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
