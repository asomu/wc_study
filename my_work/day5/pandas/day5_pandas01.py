import pandas as pd
import numpy as np
#obj1 = pd.Series([3,5,8,2])
#print(obj1)
print()
obj2 = pd.Series([3,5,8,2], index=['a','c','a','d'])
print(obj2)
'''
print(obj2.values)
print(type(obj2.values))
print()
print(obj2['c'])
obj2['c'] = 100
print(obj2)
print()
print(obj2 * 2)
print()
print(np.exp(obj2))
print()
'''
print()
print(obj2 > 7)
print()
print(obj2[obj2 > 7])

ddata = {'one':200, 'two':500, 'three':700}
print()
obj3 = pd.Series(ddata)
print(obj3)