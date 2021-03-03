import numpy as np
import pandas as pd

'''
frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
                      columns=['d','a','b','c'],
                      index=['three','one'])
print(frame1)
print()
print(frame1.sort_index(axis=0))
print()
print(frame1.sort_index(axis=1))
print()
print(frame1.sort_index(axis=1, ascending=False))


frame2 = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print(frame2)
print()
print(frame2.sort_values(by='b'))
print()
print(frame2.sort_values(by=['a','b']))
'''

frame3 = pd.DataFrame(np.random.randn(1000,2),columns=['first','second'])
print(frame3)
print(frame3.sum())
print(frame3.sum(axis=1))
print(frame3.describe())








