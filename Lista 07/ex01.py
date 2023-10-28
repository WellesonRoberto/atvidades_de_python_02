'''Usando arrays com numpy faça média das notas de uma pessoa estudante.'''

import numpy as np

notas = np.array([8.5, 6.0, 7.7, 5.0, 7.5])
media_notas = np.mean(notas)
print(f"A média é {media_notas}")
