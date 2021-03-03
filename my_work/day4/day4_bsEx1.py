from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import re

URL = "https://en.wikipedia.org/wiki/Main_Page"

pages = set()


def getLinks(pageUrl):
    html = urlopen('https://en.wikipedia.org' + pageUrl)
    bsObj = BS(html, 'html.parser')

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p'))
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('이 페이지에는 해당 속성 값이 없습니다.')

    for link in bsObj.find_all('a', href=re.compile('^/wiki/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')