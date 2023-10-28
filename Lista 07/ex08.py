'''Você é um analista de dados e possui uma matriz com os resultados de testes
realizados por diferentes usuários em um sistema. Crie um programa que utilize o
fatiamento do NumPy para contar quantos usuários obtiveram resultados positivos em
cada teste'''

import numpy as np

# Suponha que você tenha uma matriz de resultados dos testes, por exemplo:
# Cada linha representa um usuário e cada coluna representa um teste (0 para negativo, 1 para positivo)
resultados = np.array([1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0])

# Para contar quantos usuários obtiveram resultados positivos em cada teste, você pode usar np.sum
resultados_positivos_por_teste = np.sum(resultados, axis=0)

# O resultado será um array com o número de usuários que obteve um resultado positivo.

print("Resultados Positivos por Teste:")
print(f"Apenas {resultados_positivos_por_teste} usuários.")
