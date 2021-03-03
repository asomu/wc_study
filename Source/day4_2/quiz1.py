import re
from urllib.request import urlopen


f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# HTTP 헤더를 기반으로 인코딩 방식을 추출합니다(명시돼 있지 않을 경우 utf-8을 사용하게 합니다).
encoding = f.info().get_content_charset(failobj="utf-8")
# 인코딩 방식을 표준 오류에 출력합니다.
html = f.read().decode(encoding)


# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
for partial_html in re.findall(r'<td class="left"><a.+?</td>', html):
    #print(partial_html)
    # 도서의 URL을 추출합니다.
    url = re.search(r'<a href="(.+?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    # 태그를 제거해서 도서의 제목을 추출합니다.
    title = re.sub(r'<.+?>', '', partial_html)
    print('url:', url)
    print('title:', title)
    print('---')


