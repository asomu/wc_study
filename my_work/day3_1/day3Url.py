from urllib.request import urlopen
import re
'''
uf = urlopen('http://www.daum.net')
print('status: ', uf.status)
print('content-type', uf.getheader('Content-Type'))
'''

uf2 = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
byte_content = uf2.read()


scanned_text = byte_content[0:400].decode('ascii', errors='replace')


obj1 = re.search(r'charset=[\"]?([\w-]+)', scanned_text)
print(obj1.group(1))


if obj1:
    encoding = obj1.group(1)
else:
    encoding = 'utf-8'

text = byte_content.decode(encoding)
print()
print(text)
'''


charset=" "
'''
encoding = uf2.info().get_content_charset()


