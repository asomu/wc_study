from urllib.request import urlopen
import json


from_date = '2010-01-01'
to_date = '2020-12-31'

url = 'http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/'+from_date+'/edate/'+to_date

text = urlopen(url)
json_obj = json.load(text)
#print(json_obj)

pieces = []
for item in json_obj:
    print('date:{}   price:{}'.format(item['date'], item['settlement']))
    pieces.append(float(item['settlement']))

import matplotlib.pyplot as plt

plt.plot(pieces)
plt.show()