'''Indexing vs Slicing in Python'''

import numpy as np

print('''Indexing and slicing in python''')

arr = [10,20,30,40,50]

print(arr[2])      # indexing → 30
print(arr[1:4])    # slicing → [20,30,40]

'''Basic Indexing'''
arr = [10,20,30,40]

print(arr[0])     # 10 - first element
print(arr[2])     # 30 - third element
print(arr[-1])     # 40 - last element
print(arr[-2])     # 30 - second last

'''Basic Slicing'''
# Syntax: arr[start:stop:step], all start, stop and step are optional , [start, stop)
arr = [10,20,30,40,50]

print(arr[1:4])      # [20,30,40]
print(arr[:3])       # [10,20,30]
print(arr[2:])       # [30,40,50]
print(arr[:])        # copy

arr = [1,2,3,4,5,6]

print(arr[::2])      # [1,3,5]
print(arr[1::2])     # [2,4,6]

print(arr[::-1])     # [6,5,4,3,2,1] - Reverse slicing

arr = [10,20,30,40,50]
print(arr[-4:-1])    # [20,30,40] - Negative slicing


arr = [1,2,3,4]
arr[1:3] = [8,9]     # Slice assignment
print(arr)           # [1,8,9,4]  