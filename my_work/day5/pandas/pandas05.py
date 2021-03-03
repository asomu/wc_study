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
print(frame.fillna({1:1,2:-1}))