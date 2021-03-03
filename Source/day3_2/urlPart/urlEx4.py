from urllib.request import urlopen
import re

url = 'https://goo.gl/U7mSQl'
html = urlopen(url)
html_content = str(html.read().decode('utf8'))
#print(html_content)

result = re.findall(r'[a-zA-Z0-9]+\*\*\*', html_content)

for rdata in result:
    print(rdata)
