import numpy as np

# ----------------------------------------------------------
# 1️⃣ expand_dims() : Convert 2D array → 3D array
# ----------------------------------------------------------

arr_2d = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr_2d.shape)

# Output
# (2,3)
# meaning
# 2 rows
# 3 columns


# Adding new dimension at axis=0
arr_3d_a = np.expand_dims(arr_2d, axis=0)  
# axis=0 means in arr_2d.shape we got (2,3) so 0 refers to rows(i.e.,2) and 1 to columns(i.e.,3)

print(arr_3d_a.shape)

# Output
# (1,2,3)
# meaning
# 1 matrix
# 2 rows
# 3 columns


# Adding new dimension at axis=2
arr_3d_b = np.expand_dims(arr_2d, axis=2)

print(arr_3d_b.shape)

# Output
# (2,3,1)

print(f'arr_3d_b=\n{arr_3d_b}')

# So YES
# expand_dims() works for 2D → 3D


# ----------------------------------------------------------
# 2️⃣ Convert 3D array → 2D array
# ----------------------------------------------------------

arr_3d = np.array([
    [[1,2,3],
     [4,5,6]],

    [[7,8,9],
     [10,11,12]]
])

print(arr_3d.shape)

# Output
# (2,2,3)
# meaning
# 2 matrices
# each matrix 2x3


# Convert 3D → 2D using reshape
arr_2d_from3d = arr_3d.reshape(4,3)

print(arr_2d_from3d)

# Output
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# We flattened matrices into rows


# ----------------------------------------------------------
# 3️⃣ Convert 3D array → 1D array
# ----------------------------------------------------------

arr_1d = arr_3d.reshape(-1)

print(arr_1d)

# Output
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# -1 tells numpy to automatically determine dimension


# ----------------------------------------------------------
# 4️⃣ flatten() vs ravel()
# ----------------------------------------------------------

a = np.array([
    [1,2,3],
    [4,5,6]
])


# flatten() creates COPY
flat = a.flatten()

flat[0] = 999

print(flat)

# Output
# [999   2   3   4   5   6]

print(a)

# Output
# [[1 2 3]
#  [4 5 6]]

# Original array NOT changed
# because flatten() created a COPY


# ravel() creates VIEW (shares memory)

rav = a.ravel()

rav[0] = 777

print(rav)

# Output
# [777   2   3   4   5   6]

print(a)

# Output
# [[777   2   3]
#  [  4   5   6]]

# Original array CHANGED
# because ravel() shares memory with original array


# Summary
# flatten() -> copy (independent memory)
# ravel()   -> view (shared memory)


# ----------------------------------------------------------
# 5️⃣ Using np.newaxis to convert 1D → 3D
# ----------------------------------------------------------

arr_1d = np.array([1,2,3,4])

print(arr_1d.shape)

# Output
# (4,)


# Convert to 2D column vector
arr_2d = arr_1d[:, np.newaxis]

print(arr_2d.shape)

# Output
# (4,1)


# Convert to 3D
arr_3d = arr_1d[:, np.newaxis, np.newaxis]

print(arr_3d.shape)

# Output
# (4,1,1)

print(arr_3d)

# Output
# [[[1]]
#  [[2]]
#  [[3]]
#  [[4]]]


# So YES
# np.newaxis can convert 1D → 3D