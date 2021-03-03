from bs4 import BeautifulSoup

with open('US08621662-20140107.XML', 'r', encoding='utf8') as file:
    d_xml = file.read()

bsObj = BeautifulSoup(d_xml, 'lxml')

for d_info in bsObj.findAll('invention-title'):
    print(d_info.text)
