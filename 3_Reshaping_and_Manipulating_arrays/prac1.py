'''
Reshaping and Manipulating arrays:

- Reshaping : Changing the shape of an array without modifying the data.
'''
import numpy as np

# ------------------------------------------------------------
# Base array creation
# ------------------------------------------------------------

arr = np.arange(1,13)   # numbers from 1 to 12

print(arr)

# Output
# [ 1  2  3  4  5  6  7  8  9 10 11 12]


# ------------------------------------------------------------
# 1. reshape() : change array shape. Convert 1D → multi dimensional
# NOTE: Reshaping is possible only if dimensions match. Meaning total number of items in initial and final array shall match
# e.g., 1x12 can be reshaped to 4x3 or 3x4 or 2x2x3 but not to 5x3 or 7x2 or 3x1x2.
# NOTE: Reshape don't create a copy it creates a VIEW meaning any changes made to the reshaped array will be reflected in original array.
# ------------------------------------------------------------

arr2d = arr.reshape(3,4)

print(arr2d)

# Output
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

arr3d = arr.reshape(2,2,3)
print(arr3d)
# Output:
# [[[ 1  2  3]
#   [ 4  5  6]],
#  [[ 7  8  9]
#   [10 11 12]]]

# ------------------------------------------------------------
# 2. reshape with -1 (auto dimension calculation)
# ------------------------------------------------------------

arr_auto = arr.reshape(3,-1) # -1 tells numpy to automatically calculate the dimension

print(arr_auto)

# Output
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]




# ------------------------------------------------------------
# 3. Flattening array to 1D. 
# flatten() - convert to 1D copy
# ------------------------------------------------------------

flat = arr2d.flatten()

print(flat)

# Output
# [ 1  2  3  4  5  6  7  8  9 10 11 12]


# ------------------------------------------------------------
# 4. ravel() vs flatten()
# ravel() - convert to 1D view
# ------------------------------------------------------------

r = arr2d.ravel()

print(r)

# Output
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# ravel() returns VIEW (shares memory)
# flatten() returns COPY


# ------------------------------------------------------------
# 5. np_arr.T - Transpose matrix
# ------------------------------------------------------------

print(arr2d.T)

# Output
# [[ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]
#  [ 4  8 12]]


# ------------------------------------------------------------
# 6. arr.resize(). Resize array (modifies original array). Modify shape "in-place"
# ------------------------------------------------------------

arr_copy = arr.copy()

arr_copy.resize(4,3)

print(arr_copy)

# Output
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]


# ------------------------------------------------------------
# 7. Add new axis (increase dimension)
# ------------------------------------------------------------

arr_col = arr[:, np.newaxis]

print(arr_col.shape) # Now it became a column matrix  

# Output
# (12,1)

# Converts 1D array into column vector


# ------------------------------------------------------------
# 8. expand dimensions using expand_dims
# ------------------------------------------------------------

arr_expanded = np.expand_dims(arr, axis=0) # Converted 1-D array to 2-D array along x-axis with only 1 row [[1, 2, 3,...,12]]

print(arr_expanded.shape)

# Output
# (1,12)


arr_1d_to_2d_col_mat = np.expand_dims(arr, axis=1) # Convert 1-d array to 2-d array along y-axis making it a column matrix
print(arr_1d_to_2d_col_mat.shape)  # Output (12,1)


# ------------------------------------------------------------
# 9. squeeze() remove single dimension
# ------------------------------------------------------------

print(np.squeeze(arr_expanded).shape) # Converted 2-D array back to 1-D array

# Output
# (12,)

print(np.squeeze(arr_expanded)) # Converted back to 1-D array


# ------------------------------------------------------------
# 10. stacking arrays vertically
# ------------------------------------------------------------

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))

# Output
# [[1 2 3]
#  [4 5 6]]


# ------------------------------------------------------------
# 11. stacking arrays horizontally
# ------------------------------------------------------------

print(np.hstack((a,b)))

# Output
# [1 2 3 4 5 6]


# ------------------------------------------------------------
# 12. concatenate arrays
# ------------------------------------------------------------

print(np.concatenate((a,b)))

# Output
# [1 2 3 4 5 6]


# ------------------------------------------------------------
# 13. split array
# ------------------------------------------------------------

print(np.split(arr,3))

# Output
# [array([1,2,3,4]), array([5,6,7,8]), array([9,10,11,12])]


# ------------------------------------------------------------
# 14. reshape to 3D array
# ------------------------------------------------------------

arr3d = arr.reshape(2,2,3)

print(arr3d)

# Output
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]


# ------------------------------------------------------------
# 15. swap axes
# ------------------------------------------------------------

print(np.swapaxes(arr3d,0,1).shape)

# Output
# (2,2,3)
# but axis order changes


# ------------------------------------------------------------
# 16. reshape using order parameter
# ------------------------------------------------------------

print(arr.reshape(3,4, order='F'))

# Column-wise reshaping

# Output
# [[ 1  4  7 10]
#  [ 2  5  8 11]
#  [ 3  6  9 12]]


# ------------------------------------------------------------
# 17. broadcasting trick (shape manipulation)
# ------------------------------------------------------------

x = np.array([[1],[2],[3]])
y = np.array([10,20,30])

print(x + y)

# Output
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# numpy automatically expands dimensions


# ------------------------------------------------------------
# 18. reshape without modifying original array
# ------------------------------------------------------------

print(arr.shape)

# Output
# (12,)

print(arr.reshape(4,3).shape)

# Output
# (4,3)

# original arr remains unchanged