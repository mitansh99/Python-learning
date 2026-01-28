import numpy as np
# Create numpy array
array = np.array([1, 2, 3, 4])

print(array)
print(type(array)) # Output: <class 'numpy.ndarray'>

array *= 2

print(array) # Output: [2 4 6 8]

# dimensions of arrays
array = np.array('A') # one dimensional array 

array = np.array([['A', 'B', 'C'], ['D', 'E', 'F']]) # two dimensional array

array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # three dimensional array

print(array.ndim) # Output: 3 - ndim == number of dimensions
print(array.shape) # Output: (2, 2, 3) - shape == size of each dimension
print(array.size) # Output: 12 - size == total number of elements

print(array[0][0][0]) # Output: 1 - accessing elements in a 3D array - chaining method
print(array[1, 1, 2]) # Output: 12 - accessing elements in a 3D array - comma method