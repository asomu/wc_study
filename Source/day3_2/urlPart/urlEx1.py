from urllib.request import urlopen

'''
uf = urlopen('http://www.daum.net')
print(uf.read())
print('status:', uf.status)
print('content-type:', uf.getheader('Content-Type'))
'''

uf2 = urlopen('https://www.hanbit.co.kr/store/books/full_book_list.html')
#print(uf2.read())

encoding = uf2.info().get_content_charset(failobj='utf-8')
print('encoding:',encoding)

text = uf2.read().decode(encoding)
print()
print(text)
