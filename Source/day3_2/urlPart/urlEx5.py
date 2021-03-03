from urllib.request import urlopen
import re

url = "https://finance.naver.com/item/main.nhn?code=066570"
html = urlopen(url)
html_contents = str(html.read().decode('ms949'))
#print(html_contents)

stock_results = re.findall(r'(\<dl class\=\"blind\"\>([\s\S]+?)\<\/dl\>)', html_contents)
#print(stock_results)

lg_stock = stock_results[0]
#print(lg_stock)
#print(lg_stock[1])

lg_index = lg_stock[1]
index_list = re.findall(r'(\<dd\>([\s\S]+?)\<\/dd\>)', lg_index)
#index_list = re.findall(r'\<dd\>([\s\S]+?)\<\/dd\>', lg_index)
print(index_list)

for index in index_list:
    print(index[1])
