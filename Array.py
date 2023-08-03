# For creating array we use numpy library
# The array object in Numpy is called ndarray
# This object is created as soon as we create array() function

import numpy as np

arr = np.array(23)                  # 0-D Array or scalar are elements in array. Each value in an array is a 0-D array.
arr_1_d = np.array([1,2,3])         # Array that has 0-D as its element is called as uni-dimensional or 1-D Array.
print(arr_1_d.ndim)                 # Use to get dimension of any array.
# arr_2_d = np.array([[123]])
arr_2_d = np.array([[1, 2, 3], [4, 5, 6]])    # Array that has 1-D as its element is called as 2-D Array. These are often used to represent a matrix or 2nd order tensors.
print(arr_2_d.ndim)                 # Use to get dimension of any array.
arr_3_d = np.array([[[123]]])       # Array that has 2-D arrays (matrices) as its elements is called 3-D array. These are often used to represent a 3rd order tensor.
print(arr_3_d.ndim)                 # Use to get dimension of any array.


any_dim_arr = np.array([1, 2, 3, 4], ndmin=5)      # This is used to define array of any dimension using ndmin parameter
print(any_dim_arr)
print('number of dimensions :', any_dim_arr.ndim) 