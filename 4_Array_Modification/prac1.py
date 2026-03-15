import numpy as np

# ============================================================
# 1. Create Base Array
# ============================================================
print("-------------------Create Base Array-------------------")

arr = np.array([10, 20, 30, 40])
print(arr)               
# [10 20 30 40]

print(arr.shape)
# (4,)

print("-----------------------------"*3)
# ============================================================
# 2. APPEND (Add element at end)
# ============================================================
print("-------------------np.append()-------------------")

print("-------------Appending Single element-----------------------")
arr_append = np.append(arr, 50)

print(arr_append)
# [10 20 30 40 50]

print(arr_append.shape)
# (5,)


print("-------------Appending Multiple elements-----------------------")
arr_append = np.append(arr_append, [60,70,80])
print(arr_append)
# [10 20 30 40 50 60 70 80]

print("-----------------------------"*3)
# ============================================================
# 3. INSERT (Add element at specific index)
# ============================================================
print("-------------------np.insert()-------------------")

arr_insert = np.insert(arr, 2, 99)

print(arr_insert)
# [10 20 99 30 40]

print(arr_insert.shape)
# (5,)


temp_arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(f'temp_arr=\n{temp_arr}')
"""
[[10 20 30]
 [40 50 60]]
"""

print(temp_arr.shape)
# (2,3)

# ============================================================
# 3.1 INSERT WITHOUT AXIS (axis=None)
# NumPy flattens the array first
# ============================================================
print('-------------------Insert without axis-------------------')
insert_none = np.insert(temp_arr, 2, 999)

print(insert_none)
# [ 10  20 999  30  40  50  60]

print(insert_none.shape)
# (7,)

# ============================================================
# 3.2 INSERT ROW (axis = 0)
# Adds a new row
# ============================================================
print('-------------------Insert Row-------------------')
insert_row = np.insert(temp_arr, 1, [100, 200, 300], axis=0)

print(insert_row)
"""
[[ 10  20  30]
 [100 200 300]
 [ 40  50  60]]
"""

print(insert_row.shape)
# (3,3)

# ============================================================
# 3.3 INSERT COLUMN (axis = 1)
# Adds a new column
# ============================================================
print('-------------------Insert Column-------------------')

insert_col = np.insert(temp_arr, 1, [111, 222], axis=1)

print(insert_col)
"""
[[ 10 111  20  30]
 [ 40 222  50  60]]
"""

# ============================================================
# 3.4 INSERT MULTIPLE ROWS
# ============================================================
print('-------------------Insert Multiple rows-------------------')
multi_rows = np.insert(
    temp_arr,
    1,
    [[7,8,9],
     [1,2,3]],
    axis=0
)

print(multi_rows)
"""
[[10 20 30]
 [ 7  8  9]
 [ 1  2  3]
 [40 50 60]]
"""

print(temp_arr.shape)
# (4,3)

# ============================================================
# 3.5 INSERT MULTIPLE COLUMNS
# ============================================================
print('-------------------Insert Multiple Columns-------------------')

multi_cols = np.insert(
    temp_arr,
    1,
    [[9,9],
     [8,8]],
    axis=1
)

print(multi_cols)
"""
[[10  9  9 20 30]
 [40  8  8 50 60]]
"""

print(multi_cols.shape)
# (2,5)

print("-----------------------------"*3)
# ============================================================
# 4. DELETE (Remove element)
# ============================================================
print('-------------------np.delete()-------------------')

arr_delete = np.delete(arr, 1)

print(arr_delete)
# [10 30 40]

print(arr_delete.shape)
# (3,)

print("-----------------------------"*3)
# ============================================================
# 5. CONCATENATE (Join arrays)
# ============================================================
print('-------------------np.concatenate()-------------------')

a = np.array([1,2,3])
b = np.array([4,5,6])

concat = np.concatenate((a,b))

print(concat)
# [1 2 3 4 5 6]

print(concat.shape)
# (6,)

print("-----------------------------"*3)
# ============================================================
# 6. STACKING ARRAYS
# ============================================================
print('-------------------np.vstack()-------------------')
x = np.array([1,2,3])
y = np.array([4,5,6])

# Vertical stack
v_stack = np.vstack((x,y))

print(v_stack)
"""
[[1 2 3]
 [4 5 6]]
"""

print(v_stack.shape)
# (2,3)

print('-------------------np.hstack()-------------------')
# Horizontal stack
h_stack = np.hstack((x,y))

print(h_stack)
# [1 2 3 4 5 6]

print(h_stack.shape)
# (6,)

print('-------------------np.column_stack()-------------------')
# Column stack
col_stack = np.column_stack((x,y))

print(col_stack)
"""
[[1 4]
 [2 5]
 [3 6]]
"""

print(col_stack.shape)
# (3,2)

print('-------------------np.dstack()-------------------')
# Depth stack (3D stacking)
d_stack = np.dstack((x,y))

print(d_stack)
"""
[[[1 4]
  [2 5]
  [3 6]]]
"""

print(d_stack.shape)
# (1,3,2)

print("-----------------------------"*3)
# ============================================================
# 7. SPLITTING ARRAYS
# ============================================================
print('-------------------np.split()-------------------')
arr2 = np.array([1,2,3,4,5,6])

split_arr = np.split(arr2,3)

print(split_arr)
"""
[array([1,2]), array([3,4]), array([5,6])]
"""

for i in split_arr:
    print(i, i.shape)

# [1 2] (2,)
# [3 4] (2,)
# [5 6] (2,)

print("-----------------------------"*3)
# ============================================================
# 8. SPLIT 2D ARRAY
# ============================================================
print('-------------------Split 2-D array-------------------')

print('-------------------np.hsplit(): Horizontal split -------------------')
matrix = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print(matrix)
"""
[[1 2 3 4]
 [5 6 7 8]]
"""

# horizontal split
hs = np.hsplit(matrix,2)

print(hs)
"""
[array([[1,2],
        [5,6]]),
 array([[3,4],
        [7,8]])]
"""

print('-------------------np.vsplit(): vertical split-------------------')
# vertical split
vs = np.vsplit(matrix,2)

print(vs)
"""
[array([[1,2,3,4]]),
 array([[5,6,7,8]])]
"""

print("-----------------------------"*3)
# ============================================================
# 9. RESHAPE ARRAY
# ============================================================
print('-------------------np_arr.reshape()-------------------')

r = np.arange(6)

print(r)
# [0 1 2 3 4 5]

reshape_r = r.reshape(2,3)

print(reshape_r)
"""
[[0 1 2]
 [3 4 5]]
"""

print(reshape_r.shape)
# (2,3)

print("-----------------------------"*3)
# ============================================================
# 10. FLATTEN ARRAY
# ============================================================
print('-------------------np_arr.flatten()-------------------')

flat = reshape_r.flatten()

print(flat)
# [0 1 2 3 4 5]

print(flat.shape)
# (6,)

print("-----------------------------"*3)
# ============================================================
# 11. RESIZE ARRAY
# ============================================================
print('-------------------np.resize()-------------------')

resize_arr = np.resize(arr, (2,4))

print(resize_arr)
"""
[[10 20 30 40]
 [10 20 30 40]]
"""

print(resize_arr.shape)
# (2,4)

print("-----------------------------"*3)
# ============================================================
# 12. REPEAT ELEMENTS
# ============================================================
print('-------------------np.repeat()-------------------')

repeat_arr = np.repeat([1,2,3],2)

print(repeat_arr)
# [1 1 2 2 3 3]

print(repeat_arr.shape)
# (6,)

print("-----------------------------"*3)
# ============================================================
# 13. TILE ARRAY
# ============================================================
print('-------------------np.tile()-------------------')

tile_arr = np.tile([1,2,3],3)

print(tile_arr)
# [1 2 3 1 2 3 1 2 3]

print(tile_arr.shape)
# (9,)

print("-----------------------------"*3)
# ============================================================
# 14. DELETE ROW OR COLUMN FROM 2D ARRAY
# ============================================================
print('--------------------Removing from 1-D array---------------------')

temp_arr = np.array([10, 20, 30, 40, 50, 60])

print(temp_arr)
# [10 20 30 40 50 60]

print(temp_arr.shape)
# (6,)

# ============================================================
# 14.1 DELETE SINGLE ELEMENT (using index)
# ============================================================

delete_single = np.delete(temp_arr, 2)   # delete element at index 2

print(delete_single)
# [10 20 40 50 60]

print(delete_single.shape)
# (5,)

# ============================================================
# 14.2 DELETE MULTIPLE ELEMENTS (using list of indexes)
# ============================================================

delete_multiple = np.delete(temp_arr, [1, 3, 5])  

print(delete_multiple)
# [10 30 50]

print(delete_multiple.shape)
# (3,)

# ============================================================
# 14.3 DELETE ELEMENTS USING CONDITION
# ============================================================

delete_condition = temp_arr[temp_arr <= 30]  # keep only values <= 30

print(delete_condition)
# [10 20 30]

print(delete_condition.shape)
# (3,)

# ============================================================
# 14.4 DELETE USING SLICE
# ============================================================

delete_slice = np.delete(temp_arr, np.s_[2:5])   # remove index 2,3,4

print(delete_slice)
# [10 20 60]

print(delete_slice.shape)
# (3,)


print('-------------------DELETE ROW OR COLUMN FROM 2D Array-------------------')
matrix2 = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(matrix2)
"""
[[10 20 30]
 [40 50 60]
 [70 80 90]]
"""

print("-----------------------------"*3)
print('-------------------Delete row-------------------')
# delete row
delete_row = np.delete(matrix2,1,axis=0)

print(delete_row)
"""
[[10 20 30]
 [70 80 90]]
"""

print("-----------------------------"*3)
print('-------------------Delete column-------------------')
# delete column
delete_col = np.delete(matrix2,1,axis=1)

print(delete_col)
"""
[[10 30]
 [40 60]
 [70 90]]
"""

print("-----------------------------"*3)
# ============================================================
# 15. CONDITIONAL MODIFICATION
# ============================================================
print('-------------------Conditional Modification-------------------')
arr3 = np.array([10,20,30,40])

arr3[arr3 > 20] = 999

print(arr3)
# [10 20 999 999]

print(arr3.shape)
# (4,)

