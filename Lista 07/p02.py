# Indexação e Fatiamento de Arrays

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Acessando um elemento específico
elemento = arr[2]
print(f"Elemento na posição 2: {elemento}")

# Fatiamento do array
sub_array = arr[1:4]
print("\nFatiamento do array")
print(sub_array)
