'''
The best thing about numpy arrays is we can perform mathematical operations fast without using loops...

'''

# operators in python : +, -, *, /, **, //(floor division operator-for getting integral result), %

import numpy as np

print('''Arithmetic operations on numpy array''')

arr = np.array([1,3,5,7])

print(arr + 10)  # [11, 13, 15, 17]

print(arr - 1) # [0, 2, 4, 6]

print(arr * 3) # [3, 9, 15, 21]

print(arr / 2) # [0.5, 1.5, 2.5, 3.5]

print(arr // 3) # [0, 1, 1, 2]

print(arr ** 2) # [1, 9, 25, 49]

print('------------------------------------'*3)

print('''Aggregation functions practice''')

import numpy as np

# sample dataset (think of it like house prices or feature values)
arr = np.array([10, 20, 30, 40, 50])

# SUM → adds all elements
print(np.sum(arr))      
# Output: 150

# MEAN → average value
print(np.mean(arr))     
# Output: 30.0

# MEDIAN → middle value (robust against outliers)
print(np.median(arr))   
# Output: 30.0

# MIN → smallest value
print(np.min(arr))      
# Output: 10

# MAX → largest value
print(np.max(arr))      
# Output: 50

# STANDARD DEVIATION → spread of the data
print(np.std(arr))      
# Output: 14.142135623730951

# VARIANCE → square of standard deviation
print(np.var(arr))      
# Output: 200.0

# PRODUCT → multiplies all values
print(np.prod(arr))     
# Output: 12000000

# ARGMIN → index of smallest value
print(np.argmin(arr))   
# Output: 0

# ARGMAX → index of largest value
print(np.argmax(arr))   
# Output: 4

# PERCENTILE → value below which given % of data lies
print(np.percentile(arr, 50))   # 50% of data lies below 30 or we can say 30 is 50 percentile
# Output: 30.0

# COUNT NON-ZERO → counts elements that are not zero
arr2 = np.array([0, 1, 2, 0, 3])
print(np.count_nonzero(arr2))   
# Output: 3

# CUMULATIVE SUM → running total
print(np.cumsum(arr))   
# Output: [ 10  30  60 100 150]

# CUMULATIVE PRODUCT → running multiplication
print(np.cumprod(arr))  
# Output: [      10      200     6000   240000 12000000]