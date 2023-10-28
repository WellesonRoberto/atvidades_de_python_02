'''Faça um Dataframe com nome, nota1, nota2 de cinco estudantes.
Faça a média usando usando a função mean() entre as colunas nota1 e nota2.
Adicione apenas os estudante com media maior ou igual a 7 em um dataframe.
Exiba na tela esse novo dataframe apena o nome e a média'''

import pandas as pd

notas = {
    "Nome:": ["Ana", "Pedro", "Miguel", "Júlia", "Guilherme"],
    "nota1": [5.0, 6.7, 9.4, 7.3, 8.1],
    "nota2": [9.5, 6.0, 9.7, 5.6, 8.2]
}

df_notas_estudantes = pd.DataFrame(notas)

df_notas_estudantes["Média"] = df_notas_estudantes[[
    "nota1", "nota2"]].mean(axis=1)
df_aprovados = df_notas_estudantes[df_notas_estudantes["Média"] >= 7]
print(df_aprovados)
