from urllib.request import urlopen
import re
from pprint import pprint

url = 'https://finance.naver.com/item/main.nhn?code=066570'
html = urlopen(url)
html_content = str(html.read().decode('ms949'))


stock_result = re.findall(r'<dl class\=\"blind\"\>([\s\S]+?)\</dl\>', html_content)
#stock_results = re.findall(r'(\<dl class\=\"blind\"\>([\s\S]+?)\<\/dl\>)', html_contents)

#print(stock_results)
lg_stock_result = stock_result[0]


index_list = re.findall(r'(\<dd\>([\s\S]+?)\</dd\>)', lg_stock_result)
for index in index_list:
    print(index[1])