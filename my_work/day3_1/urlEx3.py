from urllib.request import urlopen
import re
from pprint import pprint
url = 'https://goo.gl/U7mSQl'

html = urlopen(url)
html_content = str(html.read().decode('utf-8'))

obj1 = re.findall(r'[\w]+\*\*\*', html_content)
pprint(obj1)