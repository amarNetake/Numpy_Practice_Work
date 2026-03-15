import numpy as np

# ============================================================
# 1️⃣ 1-D → 2-D conversion using expand_dims()
# ============================================================

arr1 = np.array([10,20,30,40])

print("Original 1D array:")
print(arr1)
print("Shape:", arr1.shape)

# Output
# [10 20 30 40]
# Shape: (4,)



# ------------------------------------------------------------
# axis = 0
# Adds a new dimension at the beginning
# ------------------------------------------------------------

arr_axis0 = np.expand_dims(arr1, axis=0)

print("\nexpand_dims(axis=0):")
print(arr_axis0)
print("Shape:", arr_axis0.shape)

# Output
# [[10 20 30 40]]
# Shape: (1,4)
#
# Meaning:
# 1 row
# 4 columns



# ------------------------------------------------------------
# axis = 1
# Adds a new dimension after the first dimension
# ------------------------------------------------------------

arr_axis1 = np.expand_dims(arr1, axis=1)

print("\nexpand_dims(axis=1):")
print(arr_axis1)
print("Shape:", arr_axis1.shape)

# Output
# [[10]
#  [20]
#  [30]
#  [40]]
# Shape: (4,1)
#
# Meaning:
# 4 rows
# 1 column



# ============================================================
# 2️⃣ 2-D → 3-D conversion using expand_dims()
# ============================================================

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nOriginal 2D array:")
print(arr2)
print("Shape:", arr2.shape)

# Output
# [[1 2 3]
#  [4 5 6]]
# Shape: (2,3)
#
# Meaning:
# 2 rows
# 3 columns



# ------------------------------------------------------------
# axis = 0
# Adds dimension before rows
# ------------------------------------------------------------

arr3_axis0 = np.expand_dims(arr2, axis=0)

print("\nexpand_dims(axis=0):")
print(arr3_axis0)
print("Shape:", arr3_axis0.shape)

# Output
# [[[1 2 3]
#   [4 5 6]]]
#
# Shape: (1,2,3)
#
# Meaning:
# 1 matrix
# 2 rows
# 3 columns



# ------------------------------------------------------------
# axis = 1
# Adds dimension between rows and columns
# ------------------------------------------------------------

arr3_axis1 = np.expand_dims(arr2, axis=1)

print("\nexpand_dims(axis=1):")
print(arr3_axis1)
print("Shape:", arr3_axis1.shape)

# Output
# [[[1 2 3]]
#
#  [[4 5 6]]]
#
# Shape: (2,1,3)
#
# Meaning:
# 2 matrices
# each matrix has
# 1 row
# 3 columns



# ------------------------------------------------------------
# axis = 2
# Adds dimension after columns
# ------------------------------------------------------------

arr3_axis2 = np.expand_dims(arr2, axis=2)

print("\nexpand_dims(axis=2):")
print(arr3_axis2)
print("Shape:", arr3_axis2.shape)

# Output
# [[[1]
#   [2]
#   [3]]
#
#  [[4]
#   [5]
#   [6]]]
#
# Shape: (2,3,1)
#
# Meaning:
# 2 rows
# 3 columns
# 1 depth layer