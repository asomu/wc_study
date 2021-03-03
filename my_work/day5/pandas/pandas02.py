import pandas as pd
import numpy as np
frame1 = pd.DataFrame([[3,2,1],[5,6,9]])
print(frame1)
print()
frame2 = pd.DataFrame([[3,2,1],[5,6,9]],
                      columns=['one','two','three'])
print(frame2)
print()
frame3 = pd.DataFrame([[3,2,1],[5,6,9]],
                      columns=['one','two','three'],
                      index=['first','second'])
print(frame3)
ddata = {'state':['seoul','seoul','daegu','suwon','busan'],
         'year':[2010,2012,2015,2017,2020],
         'pop':[2000,4000,23000,30000,21000]}
frame4 = pd.DataFrame(ddata)
print()
print(frame4)
frame5 = pd.DataFrame(ddata,
                      columns=['year','state','pop'],
                      index=['one','two','three','four','five'])
print()
print(frame5)

print()
print(frame5['state'])
print()
print(frame5.state)
print()
print(frame5.loc['two'])
print()
print(frame5['state']['two'])
print(frame5.loc['two']['state'])

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['first','second','third','fourth'],
                     columns=['one','two','three','four'])
print(frame)
print()
#print(frame.iloc[2,2])
print()
#print(frame.iloc[1:,:2])
#print()
print(frame['three'] > 5)
print()
print(frame[frame['three'] > 5]['four'])
print()
print(frame.iloc[:,2:][frame['three']>5]['four'].loc['third'])