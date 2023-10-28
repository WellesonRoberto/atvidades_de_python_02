'''Crie um programa que utilize o NumPy para realizar análises específicas sobre
as notas, como calcular a média das notas dos três primeiros alunos e verificar
quais alunos tiraram notas acima de 7'''

import numpy as np

notas = np.array([6.5, 7.1, 8.5, 6.0, 7.0, 5.0, 7.8])

media_notas = np.mean(notas[:3])
aprovados = notas[notas > 7]


print(f"A média dos três primeiros alunos foi: {media_notas:.2f}")
print(f"Notas de alunos que tiraram acima de 7,0: {aprovados}")
