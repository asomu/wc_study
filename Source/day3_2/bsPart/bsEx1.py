from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj)
