from bs4 import BeautifulSoup as BS

with open('US08621662-20140107.XML', 'r', encoding='utf-8') as file:
    content = file.read()

bsObj = BS(content, 'lxml')

for item in bsObj.find_all('invention-title'):
    print(item.text)