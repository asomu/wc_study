from bs4 import BeautifulSoup as BS

with open('books.xml','r', encoding='utf-8') as file:
    book_xml =  file.read()



bsObj = BS(book_xml, 'lxml')

for book_infor in bsObj.findAll('author'):
    print(book_infor.text)