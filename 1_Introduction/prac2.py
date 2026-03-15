'''
Various ways of Numpy arrays
'''
import numpy as np

print('''Creating numpy array Using python lists''')
arr = np.array([2,4,6,8,10])
print(arr,"\n")

print("--------------------------"*3)

print('''With default values of all zeros''')
# Syntax : np.zeros(shape)
arr = np.zeros((3))  
print(arr,"\n")  # [0, 0, 0]
arr = np.zeros((2,3))
print(arr,"\n") # [[0,0,0],[0,0,0]]

print("--------------------------"*3)

print('''With default values (all 1s)''')
# Syntax : np.ones(shape)
arr = np.ones((3))  # [1, 1, 1]
print(arr,"\n")
arr = np.ones((2,4)) # [[1,1,1,1],[1,1,1,1]]
print(arr,"\n")

print("--------------------------"*3)

print('''With default values (all ks)''')
# Syntax : np.full(shape, value)
arr = np.full((3), 10)  # [10, 10, 10]
print(arr,"\n")
arr = np.full((2,3),45) # [[45,45,45],[45,45,45]]
print(arr,"\n")

print("--------------------------"*3)

print('''Creating sequences of numbers in numpy''')
# Syntax : arange(start, stop, ,[step]) - step is optional(default step = 1). Upper bound exclusive
arr = np.arange(2,8)  # [2, 3, 4, 5, 6, 7]
print(arr,"\n")
arr = np.arange(3,15,2) # [3, 5, 7, 9, 11, 13]
print(arr,"\n")

print("--------------------------"*3)

print('''Creating identity matrices''')
# Square Matrix with 1s on the diagonal and rest all 0s
# Syntax : np.eye(n, m, k) - m is optional(if not provided or set as None it will be same as n), k is start index of diagonal which by default have value 0.
identity_Mat = np.eye(3) # Create a 3x3 identity matrix
print(identity_Mat,"\n")
# print(help(np.eye))
identity_Mat = np.eye(3, None, 1)  
'''
[[0. 1. 0.]
 [0. 0. 1.]
 [0. 0. 0.]]
'''
print(identity_Mat,"\n")

reverse_identity = np.fliplr(np.eye(3))
print(reverse_identity,"\n")
'''
[[0. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]]
'''

print("--------------------------"*3)