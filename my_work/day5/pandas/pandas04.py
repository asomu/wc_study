import numpy as np
import pandas as pd
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
print()

frame3 = pd.DataFrame(np.random.randn(1000,2),columns=['first','second'])
print(frame3)
print(frame3.sum())
print(frame3.sum(axis=1))
print(frame3.describe())