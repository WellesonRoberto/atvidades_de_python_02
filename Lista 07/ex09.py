'''Crie um programa que utilize o NumPy para calcular o retorno total do mês de
investimento e o retorno médio semanal'''

import numpy as np

# Suponha que tenhamos uma lista de retornos diários de investimento para um mês (20 dias).
retornos_diarios = [0.02, 0.01, -0.005, 0.015, 0.02, -0.01, 0.015, 0.02, 0.025, 0.03,
                    -0.02, -0.01, 0.015, 0.01, -0.005, 0.02, 0.03, -0.01, -0.02, 0.02]

# Convertemos a lista de retornos diários em um array NumPy.
retornos_diarios = np.array(retornos_diarios)

# Calcula o retorno total do mês de investimento.
retorno_total = np.prod(1 + retornos_diarios) - 1
'''1 + retornos_diarios: Primeiro, você adiciona 1 a cada um dos retornos diários. 
Isso transforma os retornos diários em fatores de crescimento. 
Por exemplo, se um dia o retorno for 0,02 (2%), você adiciona 1, resultando em 1,02, o 
que representa um aumento de 2% no investimento.

np.prod(): Esta função está calculando o produto de todos os fatores de crescimento. 

- 1: Por fim, subtrai 1 do resultado para encontrar o retorno total. A subtração é usada 
para remover a adição inicial de 1 que fizemos no primeiro passo. O valor resultante representa 
o ganho ou perda total como uma taxa percentual'''

# Calcula o retorno médio semanal.
# Supondo 5 dias úteis por semana.
retorno_medio_semanal = np.mean(retornos_diarios) * 5

# Imprime os resultados.
print(f"Retorno total do mês: {retorno_total * 100:.2f}%")
print(f"Retorno médio semanal: {retorno_medio_semanal * 100:.2f}%")
