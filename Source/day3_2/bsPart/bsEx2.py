from bs4 import BeautifulSoup

html_str = '<html><div>hello</div><div>good day</div></html>'
bsObj = BeautifulSoup(html_str, 'html.parser')
print(bsObj)
print()

print(bsObj.find('div'))
print(bsObj.find('div').text)
