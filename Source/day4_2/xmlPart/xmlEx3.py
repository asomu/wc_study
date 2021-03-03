from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'jcIDt4PJUiyQbVi14kCIL5rsq5i80l605%2FQ3TgBUlOp8I3qqrQt472uuqTPSIBL2CDvpA09wHbpr6hs3%2BCrOjg%3D%3D'

Q0 = quote_plus('서울특별시')
Q1 = quote_plus('강남')
QN = quote_plus('삼성약국')
QT = '4'
ORD = 'NAME'
pageNo= '1'
numOfRows = '10'

parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&Q1='+Q1+'&QT='+QT+'&QN='+QN+'&ORD='+ORD+'&pageNo='+pageNo+'&numOfRows='+numOfRows
url = endpoint + parameter
#print(url)

result = requests.get(url)
bsObj = BeautifulSoup(result.content, 'lxml')
items = bsObj.findAll('item')
for item in bsObj.findAll('dutyname'):
    print(item.text)
