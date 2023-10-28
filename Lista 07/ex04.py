'''Crie um programa que utilize o NumPy para calcular a média de vendas nos
primeiros 10 dias e verificar se houve algum dia em que as vendas foram maiores
que 1000. '''

import numpy as np

vendas = []

for i in range(5):
    valor = float(input(f"Digite as vendas do dia {i+1}: "))
    vendas.append(valor)

vendas = np.array(vendas)

media_vendas = np.mean(vendas[:5])

vendas_acima_mil = vendas[vendas > 1000]
print(f"Média de vendas nos 5 primeiros 5 dias: {media_vendas:.2f}")

if np.any(vendas_acima_mil):
    print("Houve pelo menos um dia com vendas acima de mil reais.")
else:
    print("Não houver vendas acima de mil reais.")
