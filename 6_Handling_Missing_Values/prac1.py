import numpy as np

# ============================================================
# 1. CREATE ARRAY WITH MISSING VALUES
# ============================================================

data = np.array([10, 20, np.nan, 40, np.nan, 60])

print(data)
# [10. 20. nan 40. nan 60.]

print(data.shape)
# (6,)


# ============================================================
# 2. DETECT MISSING VALUES
# ============================================================

print(np.isnan(data))

# [False False  True False  True False]


# ============================================================
# 3. COUNT MISSING VALUES
# ============================================================

print(np.isnan(data).sum())

# 2


# ============================================================
# 4. REMOVE MISSING VALUES
# ============================================================

clean_data = data[~np.isnan(data)]

print(clean_data)

# [10. 20. 40. 60.]

print(clean_data.shape)

# (4,)


# ============================================================
# 5. REPLACE NaN WITH CONSTANT VALUE
# ============================================================

filled_constant = np.nan_to_num(data, nan=0)

print(filled_constant)

# [10. 20.  0. 40.  0. 60.]


# ============================================================
# 6. REPLACE NaN USING CONDITIONAL INDEXING
# ============================================================

data_copy = data.copy()

data_copy[np.isnan(data_copy)] = -1

print(data_copy)

# [10. 20. -1. 40. -1. 60.]


# ============================================================
# 7. REPLACE NaN WITH MEAN
# ============================================================

data2 = np.array([10, 20, np.nan, 40, 50])

mean_val = np.nanmean(data2)

data2[np.isnan(data2)] = mean_val

print(data2)

# [10. 20. 30. 40. 50.]


# ============================================================
# 8. REPLACE NaN WITH MEDIAN
# ============================================================

data3 = np.array([10, np.nan, 30, 40, np.nan])

median_val = np.nanmedian(data3)

data3[np.isnan(data3)] = median_val

print(data3)

# [10. 30. 30. 40. 30.]


# ============================================================
# 9. NUMPY NAN-SAFE AGGREGATION FUNCTIONS
# ============================================================

arr = np.array([10, 20, np.nan, 40])

print(np.nanmean(arr))
# 23.333333333333332

print(np.nansum(arr))
# 70.0

print(np.nanmax(arr))
# 40.0

print(np.nanmin(arr))
# 10.0

print(np.nanstd(arr))
# standard deviation ignoring NaN


# ============================================================
# 10. HANDLE NaN IN 2D ARRAY
# ============================================================

matrix = np.array([
    [10, 20, np.nan],
    [40, np.nan, 60],
    [70, 80, 90]
])

print(matrix)

"""
[[10. 20. nan]
 [40. nan 60.]
 [70. 80. 90.]]
"""


# ============================================================
# 11. REMOVE ROWS WITH NaN
# ============================================================

rows_without_nan = matrix[~np.isnan(matrix).any(axis=1)]

print(rows_without_nan)

"""
[[70. 80. 90.]]
"""


# ============================================================
# 12. REMOVE COLUMNS WITH NaN
# ============================================================

cols_without_nan = matrix[:, ~np.isnan(matrix).any(axis=0)]

print(cols_without_nan)

"""
[[10.]
 [40.]
 [70.]]
"""


# ============================================================
# 13. FILL NaN COLUMN-WISE WITH MEAN
# ============================================================

matrix2 = np.array([
    [10, 20, np.nan],
    [40, np.nan, 60],
    [70, 80, 90]
])

col_mean = np.nanmean(matrix2, axis=0)

print(col_mean)

# [40. 50. 75.]

# Replace NaNs with column means
inds = np.where(np.isnan(matrix2))

matrix2[inds] = np.take(col_mean, inds[1])

print(matrix2)

"""
[[10. 20. 75.]
 [40. 50. 60.]
 [70. 80. 90.]]
"""


# ============================================================
# 14. MASKED ARRAYS (IGNORE NaN IN CALCULATIONS)
# ============================================================

masked = np.ma.masked_invalid(data)

print(masked)

# [10.0 20.0 -- 40.0 -- 60.0]

print(masked.mean())

# mean ignoring missing values


# ============================================================
# 15. INTERPOLATION (FILL MISSING USING NEIGHBORS)
# ============================================================

arr_interp = np.array([10, np.nan, np.nan, 40])

# indices
nans = np.isnan(arr_interp) # [False True True False]
x = np.arange(len(arr_interp)) # [0 1 2 3]

# x[nans] becomes [1 2] मतलब हमें index 1 और 2 पर values चाहिए। Meaning index 1 and index 2 has missing values
# x[~nans] becomes [0 3] मतलब known values कहाँ हैं।
# arr_interp[~nans] becomes [10 40] मतलब known values।
arr_interp[nans] = np.interp(x[nans], x[~nans], arr_interp[~nans])
# np.interp(
#    [1,2],   # where values are missing
#    [0,3],   # known positions
#    [10,40])  # known values
# NumPy अब line बनाता है:
# (0,10)  →  (3,40)
# (40 - 10) / (3 - 0) = 30 / 3 = 10
#arr_interp[nans] = [20 30] 
# => arr_interp = [10 20 30 40]

print(arr_interp)

# [10. 20. 30. 40.]


# ============================================================
# 16. USING WHERE TO REPLACE NaN
# ============================================================

arr4 = np.array([10, np.nan, 30, np.nan])

result = np.where(np.isnan(arr4), 0, arr4)

print(result)

# [10.  0. 30.  0.]


# ============================================================
# 17. NOTE: 2 Nan values are never equal
# ============================================================

print(np.nan == np.nan)  # False