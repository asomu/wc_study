import numpy as np

arr1 = np.arange(10)
'''
print(np.sqrt(arr1))
print(np.exp(arr1))
print(np.cos(arr1))

print()
'''

data1 = [[1,2,3,4],
         [2,34,5,6],
         [24,2,3,4]]
arr1 = np.array(data1)

print('sum: ' , arr1.sum())
print('meas: ' , arr1.mean())

print(arr1.sum(axis=0))

arr3 = np.arange(12)
print(arr3)
print(arr3.reshape((4,3)))





