import numpy as np

'''Attributes'''


print('''Finding shape, size and type, number of dimensions of numpy array''')
arr_2d = np.array([[1,2,3],
                   [4,5,6]])

arr_3d = np.array([[[1,2],[2,3]],
                   [[4,5],[6,7]],
                   [[7,8],[9,10]]])

arr = np.array(["Amar", "Jeet", "Krish", "Deepak"])

print(f'arr_2d=\n{arr_2d}')
# To get the shape of numpy array use:  np_arr.shape
print(f'arr_2d.shape = {arr_2d.shape}')  # arr_2d.shape = (2,3)
print(f'arr_3d.shape = {arr_3d.shape}')  # arr_3d.shape = (3,2,2)

# To get total number of items in the numpy array : np_arr.size 
print(f'arr_2d.size = {arr_2d.size}')  # arr_2d.size = 6

# To check the number of dimensions : np_arr.ndim
print(f'arr_2d.ndim = {arr_2d.ndim}')   # arr_2d.ndim = 2
print(f'arr_3d.ndim = {arr_3d.ndim}')   # arr_3d.ndim = 3

# To check the data types of elements : np_arr.dtype
print(f'arr_2d.dtype={arr_2d.dtype}')  # arr_2d.dtype = int64
print(f'arr_3d.dtype={arr_3d.dtype}')  # arr_3d.dtype = int64
print(f'arr.dtype={arr.dtype}')  # arr.dtype = <U6 where 
# < tells it is Little-endian byte order, U -> Unicode string, 6 -> Length of longest string in the array. So it means "Unicode strings up to length 6".

# arr = np.array([2,3,[4,5]])
# print(arr)  # ValueError as numpy array has to be homogeneous

print("----------------------------------"*3)

print('''Convert data type of elements of numpy array from one type to another''')
# Syntax: np_array.astype()
arr = np.array(['23','0','31','49'])

print(arr)

arr = arr.astype(int)

print(arr)

arr = arr.astype(float)

print(f'arr={arr}, arr.dtype={arr.dtype}')

bool_arr = arr.astype(bool)

print(bool_arr)

arr = arr.astype(str)

print(arr)

arr = np.array([1.2, 4.57, 3.4, 5.0, 6.82])

print(arr)

arr = arr.astype(int)

print(arr)