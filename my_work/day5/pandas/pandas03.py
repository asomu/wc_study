import pandas as pd
df1 = pd.read_csv('ex1.csv')
print(df1)
print(type(df1))
print()
df2 = pd.read_csv('ex2.csv', header=None)
print(df2)
print()
df3 = pd.read_csv('ex2.csv', names=['one','two','three','four','info'])
print(df3)
print()
df4 = pd.read_csv('ex2.csv',
                  names=['one','two','three','four','info'],
                  index_col='info')
print(df4)
df4.columns.name = 'data'
print()
print(df4)
print()
df5 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
print(df5)

import numpy as np
frame = pd.DataFrame(np.random.randn(1000,3),
                     columns=['first','second','third'])
print(frame)
print(frame.info())
print()
print(frame.head(10))
print()
print(frame.tail(10))