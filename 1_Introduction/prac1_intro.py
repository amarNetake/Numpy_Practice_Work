import numpy as np

temperatures = np.array([32.5, 31.8, 33.0, 35.2, 36])

average = np.mean(temperatures)

print(average)

# 1-D array
arr_1D = np.array([10,20,30,40,50])
print(f"arr_1D = {arr_1D}")

# 2-D array
arr_2D = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(f"arr_2D = \n{arr_2D}")
print(arr_2D.shape)

# Multi-dimensional array(matrix)
matrix = np.array([[2,4,6],
                   [8,10,12]])
print(f"matrix = \n{matrix}")
print(matrix.shape)

arr_3D = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
print(f"arr_3D = \n{arr_3D}")
print(arr_3D.shape)
