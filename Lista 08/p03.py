'''Crie um DataFrame que represente informações sobre estudantes, incluindo nome, idade, e média de notas.
Em seguida, realize as seguintes tarefas:
Crie um DataFrame com os seguintes dados:
● Nome
● Média de Notas: 8.5, 7.8, 9.2, 6.5, 8.9
● Adicione uma coluna chamada "Status" que contenha "Aprovado" para estudantes com média de notas
maior ou igual a 7.0 e "Reprovado" para os demais.
● Selecione apenas os estudantes "Aprovados" e crie um novo DataFrame com esses dados.'''

import pandas as pd

estudantes = [["Ana", 8.5],
              ["Pedro", 7.8],
              ["Caio", 6.2],
              ["Vanessa", 6.5],
              ["Miguel", 8.9]]


df_alunos = pd.DataFrame(estudantes, columns=["Aluno", "Média"])

status = ["Aprovado", "Aprovado", "Reprovado", "Reprovado", "Aprovado"]
df_alunos["Status"] = status

df_reprovados = df_alunos[df_alunos["Status"] == "Reprovado"]
print(df_reprovados)
