# Operações Matemáticas em Arrays

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr3 = np.array([1, 2, 3])
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
arr5 = np.array([10, 20, 30])

# Soma de arrays
soma = arr1 + arr2
print(f"Soma dos arrays: {soma}")
print()

# Subtração dos arrays elemento a elemento
subtracao = arr2 - arr1
print(f"Subtração dos arrays: {subtracao}")
print()


# Multiplicação de arrays
produto = arr1 * arr2
print(f"Produto dos arrays: {produto}")
print()


# Divisão de arrays elemento a elemento
divisao = arr1/arr2
print(f"Divisão dos arrays: {divisao}")
print()

# Exponenciação dos elementos do array
exponeciacao = np.power(arr3, 2)
print(f"Exponenciação: {exponeciacao}")
print()

# Soma dos elementos do array
soma2 = np.sum(arr1)
print(f"Soma dos elementos do arr1: {soma2}")
print()

# Valor máximo do array
maximo = np.max(arr2)
print(f"O valor máximo do arr2: {maximo}")
print()

# Valor mínimo do array
minimo = np.min(arr2)
print(f"O valor mínimo do arr2: {minimo}")
print()

# Média dos elementos do array
media = np.mean(arr1)
print(f"A média do arr1: {media}")
print()

# Broadcasting
resultado = arr4 + arr5
print("Resultado após broadcasting: ")
print(resultado)
print()
