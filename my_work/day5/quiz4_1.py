from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

seoul = '서울특별시'

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'jcIDt4PJUiyQbVi14kCIL5rsq5i80l605%2FQ3TgBUlOp8I3qqrQt472uuqTPSIBL2CDvpA09wHbpr6hs3%2BCrOjg%3D%3D'
Q0 = quote_plus('서울특별시')
ORD = 'NAME'
pageNo = '1'
numberOfRows = '5000'


paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&ORD="+ORD+"&pageNo="+pageNo+"&numOfRows="+numberOfRows

url = endpoint + paramset
print(url)

result = requests.get(url)

bs_obj = BeautifulSoup(result.content, 'lxml')
items = bs_obj.findAll('item')

count = 0
for item in items:
    tag_item = item.find('dutytime1c')
    if(tag_item != None):
        close_time = int(tag_item.text)
        if(close_time > 2100):
            count +=1
print('월요일 9시 이후까지 하는 약국의 수:'+ str(count))
