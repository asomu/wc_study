import pandas as pd

danawa_data = pd.read_csv('./../files/danawa_final.csv')

top_suction = danawa_data.sort_values(['흡입력'], ascending=False)
#print(top_suction)
top_utime = danawa_data.sort_values(['사용시간'], ascending=False)
#print(top_utime)
top_utime_suction = danawa_data.sort_values(['사용시간', '흡입력'], ascending=False)
print(top_utime_suction.head(20))
print()
print('가격 평균 값:', danawa_data['가격'].mean())
print('흡입력 평균 값:', danawa_data['흡입력'].mean())
print('사용시간 평균 값:', danawa_data['사용시간'].mean())
