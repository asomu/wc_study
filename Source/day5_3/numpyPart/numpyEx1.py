import numpy as np

data1 = [6,7,8,0,1]
arr1 = np.array(data1)
print(data1)
print(arr1)
print(type(arr1))

data2 = [[1,2,3,4],[5,6,'7',8]]
arr2 = np.array(data2, dtype=np.float32)
print()
print(arr2)
print()

print(arr2.shape)
print(arr2.dtype)

arr3 = np.array([[1,2,3,4],[5,6,7,8]], dtype=np.float32)
print()
print(arr3)
print(arr3.dtype)

arr4 = arr3.astype(np.int64)
print(arr4.dtype)
