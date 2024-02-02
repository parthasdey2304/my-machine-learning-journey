import numpy as np

arr_1 = np.array([1, 2, 3, 4, 5]) # 1D array creation
arr_2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array creation

# Printing both the arrays
print(arr_1)
print(arr_2)

print(arr_1.shape) # Output: (5,)
print(arr_2.shape) # Output: (2, 3)
print(arr_2.dtype) # Prints the data types of the arrays Output: int64
print(arr_2.ndim) # Prints the number of dimensions of the axes

