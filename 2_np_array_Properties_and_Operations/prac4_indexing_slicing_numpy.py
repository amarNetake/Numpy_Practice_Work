'''Indexing and slicing in numpy'''

import numpy as np

print('''1-D Array indexing''')

arr = np.array([10,20,30,40])
# Syntax: arr[index]
print(arr[0])  # 10
print(arr[-1])  # 40


print('''1-D Array Slicing''')
arr = np.array([10,20,30,40])
print(arr[:]) # [10,20,30,40]
print(arr[:2]) # [10,20]
print(arr[1:]) # [20,30,40]
print(arr[::-1]) # [40,30,20,10]
print(arr[::-2]) # [40,20]
print(arr[::2]) # [10,30]


print('''2-D array indexing''')
# Syntax: arr[row, col]
arr = np.array([
 [1,2,3],
 [4,5,6],
 [7,8,9]
])

print(arr[1,2])  # 6
print(arr[0,1])  # 2  -> faster
print(arr[0][1]) # 2 -> Equivalent to arr[0,1] but is slower


print('''Slicing in 2-D array''')
# Row Slicing
print(arr[0])        # [1,2,3] - first row
print(arr[2])        # [7,8,9]
print(arr[1:])       # [[4,5,6],[7,8,9]] - rows 1 onwards

# Column slicing
print(arr[:,1])      # [2,5,8]
print(arr[:2, 1])    # [2,5]
print(arr[:1, 1])    # [2]
print(arr[1:, 1])    # [5,8]

print('----------------------------------'*3)

print('''Boolean masking''')

ages = np.array([16,18,25,48,23,31,12,51,7,33,26,44])

# Select players with ages greater than 18 only
print(ages[ages >= 18])  # [18 25 48 23 31 33 26]

# Select players with ages greater than or equal to 18 and less than 40
print(ages[(ages >= 18) & (ages < 40)])  # [18 25 23 31 33 26]

# Select players with ages less than 18 or greater than 40
print(ages[(ages < 18) | (ages > 40)])   # [16 48 12 51  7 44]

# Players with age not 18
print(ages[~(ages==18)])  # [16 25 48 23 31 12 51  7 33 26 44]

arr = np.array([
 [10,20,30],
 [40,50,60]
])

result = arr[(arr > 20) & (arr < 60)]

print(result)

print('----------------------------------'*3)

print('''Fancy Indexing''')

arr1 = np.array([10,20,30,40,50])

'''Select elements at index positions 0,2,4'''
print(arr1[[0,2,4]]) # [10 30 50]

'''Fancy indexing with repeated indices'''
print(arr1[[1,1,3]])  # [20 20 40]

'''Row selection in 2D array'''
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arr[[0,2]]) # Notice here we are using double brackets
# Output
# [[10 20 30]
#  [70 80 90]]

'''Column selection using fancy indexing'''
print(arr[:, [0,2]])
# Output
# [[10 30]
#  [40 60]
#  [70 90]]

'''Selecting specific elements using coordinate pairs'''
print(arr[[0,1,2], [2,1,0]])
# Coordinates selected:
# (0,2) -> 30
# (1,1) -> 50
# (2,0) -> 70

# Output
# [30 50 70]

'''Selecting submatrix using fancy indexing'''
print(arr[[0,2]][:, [0,2]])
# Steps:
# first select rows [0,2]
# then select columns [0,2]

# Output
# [[10 30]
#  [70 90]]

'''Fancy indexing using another array of indices'''
indices = np.array([0,2])

print(arr1[indices])
# Output
# [10 30]



