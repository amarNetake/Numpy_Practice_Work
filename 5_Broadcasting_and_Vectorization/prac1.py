'''
Broadcasting = NumPy automatically expands smaller arrays so operations can happen without manual looping.

Benefits of Broadcasting:
- No loops required 
- Looping is slow, this is super fast as no looping (python loops are run by python interpreter, Numpy broadcasting is run by Optimized C, thus Numpy Broadcasting is blazingly fast)
- memory efficient : छोटा array physically copy नहीं होता। बल्कि calculation के समय virtual expansion करता है।

Think of it like this:

Array      : [1 2 3]
Scalar     : 10

print(arr + 10)

[1 2 3] + 10

NumPy internally ऐसा समझता है:

[1 2 3] + [10 10 10]

Result     : [1+10, 2+10, 3+10]
           = [11 12 13]

NOTE: लेकिन वह memory में नया array नहीं बनाता, बस calculation के समय expand मान लेता है।

Here 10 is broadcasted to match the array shape.

Broadcasting Rules

NumPy compares shapes from right → left.

Two dimensions are compatible if:

1️⃣ They are equal
or
2️⃣ One of them is 1

Example:

(3,1) + (1,4) -> This will Broadcasts to (3,4)

//Otherwise
A = np.ones((3,2))
B = np.ones((2,3))

print(A + B) //ValueError because dimensions of A and B are not same and neither dimensions are 1

A = np.array([10,20,30])
B = np.array([40,50])

print(A + B) //ValueError, Dimensions are not equal and neither dimensions are 1.

----------------------------------------------------------------------------------------------------

2. Vectorization (Simple Explanation)

Vectorization = performing operations on entire arrays instead of loops.

Bad way (slow):

for i in range(n):
    result[i] = a[i] + b[i]

Good way (vectorized):

result = a + b

Why?
Because NumPy runs optimized C code internally, which is 10-100x faster.
'''

import numpy as np


# ==========================================================
# 1. SCALAR BROADCASTING
# ==========================================================

arr = np.array([1,2,3,4])

result = arr + 10   # scalar automatically expands

print(result)
# [11 12 13 14]


# ==========================================================
# 2. VECTOR VECTORIZATION (element-wise operation)
# ==========================================================

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
# [5 7 9]

print(a * b)
# [ 4 10 18]

print(a ** 2)
# [1 4 9]


# ==========================================================
# 3. BROADCASTING WITH ROW VECTOR
# ==========================================================

matrix = np.array([
    [10,20,30],
    [40,50,60]
])

row = np.array([1,2,3])

result = matrix + row

print(result)

"""
[[11 22 33]
 [41 52 63]]
"""


# ==========================================================
# 4. BROADCASTING WITH COLUMN VECTOR
# ==========================================================

col = np.array([[1],[2]])

result = matrix + col

print(result)

"""
[[11 21 31]
 [42 52 62]]
"""


# ==========================================================
# 5. BROADCASTING DIFFERENT SHAPES
# ==========================================================

a = np.array([[1],[2],[3]])   # shape (3,1)
b = np.array([10,20,30,40])   # shape (4,)

result = a + b

print(result)

"""
[[11 21 31 41]
 [12 22 32 42]
 [13 23 33 43]]
"""

# broadcasting produced shape (3,4)


# ==========================================================
# 6. VECTORISED COMPARISON
# ==========================================================

arr = np.array([5,10,15,20])

mask = arr > 10

print(mask)
# [False False  True  True]

print(arr[mask])
# [15 20]


# ==========================================================
# 7. CONDITIONAL VECTORIZATION (np.where)
# ==========================================================

arr = np.array([10,20,30,40])

result = np.where(arr > 25, 1, 0)

print(result)
# [0 0 1 1]


# ==========================================================
# 8. VECTORISED MATH FUNCTIONS
# ==========================================================

arr = np.array([1,4,9,16])

print(np.sqrt(arr))
# [1. 2. 3. 4.]

print(np.log(arr))
# [0.         1.38629436 2.19722458 2.77258872]

print(np.exp(arr))
# exponential values


# ==========================================================
# 9. OUTER OPERATIONS USING BROADCASTING
# ==========================================================

a = np.array([1,2,3])
b = np.array([10,20,30])

outer_sum = a[:,None] + b

print(outer_sum)

"""
[[11 21 31]
 [12 22 32]
 [13 23 33]]
"""


# ==========================================================
# 10. VECTORISED NORMALIZATION
# ==========================================================

data = np.array([10,20,30,40])

normalized = (data - np.mean(data)) / np.std(data)

print(normalized)

# [-1.34164079 -0.4472136   0.4472136   1.34164079]


# ==========================================================
# 11. DISTANCE COMPUTATION (vectorized)
# ==========================================================

points = np.array([
    [1,2],
    [3,4],
    [5,6]
])

target = np.array([1,1])

distances = np.sqrt(np.sum((points - target)**2, axis=1))

print(distances)
# [1.         3.60555128 6.40312424]


# ==========================================================
# 12. 3D BROADCASTING
# ==========================================================

a = np.ones((2,3,4))
b = np.array([1,2,3,4])

result = a * b

print(result.shape)
# (2,3,4)

# b broadcasted across last dimension


# ==========================================================
# 13. VECTORISED CLIPPING
# ==========================================================

arr = np.array([-10,5,20,100])

print(np.clip(arr,0,50))

# [ 0  5 20 50]


# ==========================================================
# 14. VECTORIZED SUMMATION
# ==========================================================

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

print(matrix.sum(axis=0))
# [5 7 9]

print(matrix.sum(axis=1))
# [ 6 15]


# ==========================================================
# 15. BROADCASTING FOR FEATURE SCALING (ML usecase)
# ==========================================================

data = np.array([
    [10,200],
    [20,400],
    [30,600]
])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

scaled = (data - mean) / std

print(scaled)

"""
[[-1.22474487 -1.22474487]
 [ 0.          0.        ]
 [ 1.22474487  1.22474487]]
"""

'''
Broadcasting is used for:-
- feature scaling
- matrix operations
- distance calculations
- deep learning tensor operations

Vectorization is used for:-
- removing loops
- faster ML computations
- large dataset processing

One Important Trick used everywhere in ML frameworks:
x = np.array([1 2 3])

x[:, None] will give: 
[[1]
 [2]
 [3]]
'''
print("----------Hello-----------")
x = np.array([1,2,3])

print(x)

print(x[:,None])



