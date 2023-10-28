# Arrays unidimensionais, bidimensionais e multidimensionais.

import numpy as np

# Array unidimensional
arr1 = np.array([1, 2, 3, 4, 5])
print("\nArray unidimensional:")
print(arr1)

# Array bidimensional
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray bidimensional:")
print(arr2)

# Array com valores zeros
zeros_arr = np.zeros((3, 4))
print("\nArray com valores zeros:")
print(zeros_arr)

# Array com valores aleatórios entre 0 e 1
random_arr = np.random.rand(2, 3)
print("\nArray com valores aleatórios:")
print(random_arr)
