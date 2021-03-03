import pandas as pd
import numpy as np

sobj = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(sobj)
print()
print(sobj.dropna())
print()
print(sobj[sobj.notnull()])

frame = pd.DataFrame(np.random.randn(7,3))
print()
frame.iloc[:4,1] = np.nan
frame.iloc[:2,2] = np.nan
print(frame)

print()
print(frame.fillna(0))
print()
print(frame.fillna({1:0, 2:-1}))
print()
print(frame.fillna(method='backfill'))
print()
print(frame.fillna(frame.mean()))
