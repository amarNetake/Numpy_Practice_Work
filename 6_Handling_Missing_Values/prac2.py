import numpy as np

# ============================================================
# 1. CREATE ARRAY WITH INFINITE VALUES
# ============================================================

arr = np.array([10, 20, np.inf, 40, -np.inf, 60])

print(arr)
# [ 10.  20.  inf  40. -inf  60.]

print(arr.shape)
# (6,)


# ============================================================
# 2. IDENTIFY INFINITE VALUES
# ============================================================

print(np.isinf(arr))

# [False False  True False  True False]


# ============================================================
# 3. COUNT INFINITE VALUES
# ============================================================

print(np.isinf(arr).sum())

# 2


# ============================================================
# 4. IDENTIFY POSITIVE INFINITY
# ============================================================

print(np.isposinf(arr))

# [False False  True False False False]


# ============================================================
# 5. IDENTIFY NEGATIVE INFINITY
# ============================================================

print(np.isneginf(arr))

# [False False False False  True False]


# ============================================================
# 6. KEEP ONLY FINITE VALUES
# ============================================================

finite_values = arr[np.isfinite(arr)]

print(finite_values)

# [10. 20. 40. 60.]


# ============================================================
# 7. REMOVE INFINITE VALUES
# ============================================================

clean_arr = arr[~np.isinf(arr)]

print(clean_arr)

# [10. 20. 40. 60.]


# ============================================================
# 8. REPLACE INF VALUES WITH CONSTANT
# ============================================================

arr_copy = arr.copy()

arr_copy[np.isinf(arr_copy)] = 0

print(arr_copy)

# [10. 20.  0. 40.  0. 60.]


# ============================================================
# 9. CONVERT INF TO NaN
# ============================================================

arr_copy2 = arr.copy()

arr_copy2[np.isinf(arr_copy2)] = np.nan

print(arr_copy2)

# [10. 20. nan 40. nan 60.]


# ============================================================
# 10. HANDLE INF USING nan_to_num()
# ============================================================

arr_fixed = np.nan_to_num(arr, posinf=999, neginf=-999)

print(arr_fixed)

# [ 10.  20. 999.  40. -999.  60.]


# ============================================================
# 11. CHECK BOTH NaN AND INF TOGETHER
# ============================================================

arr2 = np.array([10, np.nan, np.inf, -np.inf, 50])

print(arr2)
# [ 10.  nan  inf -inf  50.]

print(np.isfinite(arr2))

# [ True False False False  True]

print(arr2[np.isfinite(arr2)])

# [10. 50.]