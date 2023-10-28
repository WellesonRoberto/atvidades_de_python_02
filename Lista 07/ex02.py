'''Crie um programa que utilize arrays com NumPy para armazenar os dados de
temperatura média diária de uma cidade nos últimos sete dias e calcule a
temperatura média e a temperatura máxima e mínima registrada nesse período.'''

import numpy as np

temperaturas = np.array([25.0, 28.0, 35.0, 29.0, 31.5, 32.6, 37.0])

media_temperaturas = np.mean(temperaturas)
max_temperaturas = np.max(temperaturas)
min_temperaturas = np.min(temperaturas)

print(f"Média das temperaturas {media_temperaturas:.2f}")
print(f"Máxima das temperaturas {max_temperaturas}")
print(f"Mínima das temperaturas {min_temperaturas}")
