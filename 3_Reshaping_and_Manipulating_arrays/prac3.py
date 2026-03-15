# I still don't get the axis part what axis=2 and axis=0 means, it is already to difficult to picture in brain.

'''Axis simply means "direction of indexing"'''

#Take a 2-D array:

import numpy as np

arr = np.array([
 [1,2,3],
 [4,5,6]
])

print(arr.shape) # (2,3) 
# => 2 rows & 3 columns
# => axis=0 → rows(Operate between rows)
#    axis=1 → columns(Operate between columns)

# axis=0  ↓
#[[1 2 3]
# [4 5 6]]
# axis=1 →

print(arr.sum(axis=0)) # Output: [5 7 9]. Sum down the rows
#1+4
#2+5
#3+6
print(arr.sum(axis=1)) #Output: [6,15]. Sum along the columns

print("----------------------------"*3)

'''Now look at a 3-D array'''

arr3d = np.array([
 [[1,2,3],
  [4,5,6]],

 [[7,8,9],
  [10,11,12]]
])

print(arr3d.shape) # (2,2,3) =>
#2 matrices
#each matrix → 2 rows
#each row → 3 columns

# axis=0 → along matrix. Two items at same position across the outer matrix will be operated
# axis=1 → along row. Items along the row of same matrix will be operated
# axis=2 → along column. Items along the column of same matrix will be operated

print(arr3d.sum(axis=0)) # Output=
#[[ 8 10 12]
# [14 16 18]]

print(arr3d.sum(axis=1)) # Output=
# [[ 5  7  9]
#  [17 19 21]]

print(arr3d.sum(axis=2)) # Output=
# [[ 6 15]
#  [24 33]]