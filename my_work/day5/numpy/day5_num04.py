import numpy as np
arr1 = np.array([5,2,6,3,9,8])
print(arr1)
print(arr1[2])
print(arr1[:4])
arr1[2] = 100
print(arr1)
arr2 = np.array([[2,  4,  5,  9],
                 [10, 60, 70, 80],
                 [500,700,400,100]])
print()
print(arr2)
print()
print(arr2[1][1])
print(arr2[1, 1])
print()
print(arr2[1:, 2:])
print()
print(arr2[1:][2:])