#도서제목과 링크 가져오기
#정규식으로 가져오기.
#url:
#tile:
#---

from urllib.request import urlopen
import re

url = "https://www.hanbit.co.kr/store/books/full_book_list.html"

html = urlopen(url)
html_contents = html.read().decode('utf-8')

obj = re.findall(r'<a href="(/store/books/look.php\?p_code=[\w]+)\"\>([\w가-힝\s,]*)', html_contents)
for item in obj:
    print(f"url: https://www.hanbit.co.kr{item[0]}")
    print(f"title: {item[1]}")
    print("-----")
