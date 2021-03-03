from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://www.pythonscraping.com/pages/page1.html'

url2 = """
<html>
    <body>
        <ul class='ok'>
            <li>
                <a href='https://www.naver.com/'>네이버</a>
            </li>
            <li>
                <a href='https://www.daum.net/'>다음</a>
            </li>
            <li>welcome</li>
        </ul>
        <ul class='sns'>
            <li>
                <a href='https://www.google.com/'>구글</a>
            </li>
            <li>
                <a href='https://www.facebook.com/'>페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""


html = urlopen(url)
bs4 = BeautifulSoup(url2, 'html.parser')

atag = bs4.find_all('a')
url = []
name = []
for item in atag:
    url.append(item['href'])
    name.append(item.text)
print(url)
print(name)