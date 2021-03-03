from urllib.parse import quote_plus
from bs4 import BeautifulSoup as BS
import requests


endPoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'jcIDt4PJUiyQbVi14kCIL5rsq5i80l605%2FQ3TgBUlOp8I3qqrQt472uuqTPSIBL2CDvpA09wHbpr6hs3%2BCrOjg%3D%3D'

Q0 = quote_plus('서울특별시')
Q1 = ''
QN = ''
QT = '4'
ORD = 'NAME'
page_number = '1'
number_of_rows = '5000'

#parameter ='serverKey=' + serverKey + '&Q0=' + Q0 + '&Q1' + Q1 + '&QT' + QT + '&QN' + QN + '&ORD' + QRD + '&pageNo=' +page_number + '&numOfRows=' + number_of_rows
parameter = 'serviceKey='+serviceKey+'&Q0='+Q0+'&Q1='+Q1+'&QT='+QT+'&QN='+QN+'&ORD='+ORD+'&pageNo='+page_number+'&numOfRows='+number_of_rows
url = endPoint  + parameter
result = requests.get(url)

bsObj = BS(result.content, 'lxml')
cnt = 0
for name in bsObj.find_all('dutytime1c'):
    if int(name.text) > 2100:
        cnt += 1

print(cnt)
