'''Crie um DataFrame representando com as notas de cinco pessoas estudantes
em diferentes disciplinas. Calcule a média de cada estudante e adicione uma
coluna chamada "Média" ao DataFrame. Em seguida, crie um novo DataFrame
apenas com os alunos que obtiveram uma média menor do que 7.0. '''

import os
import pandas as pd

os.system("cls")

# CRIANDO DICIONARIO
dict_notas = {
    'Nome': ['Juliana', 'Marcos', 'Matheus', 'Luana'],
    'Matematica': [10.0, 6.5, 8.0, 7.0],
    'Portugues': [8.0, 7.0, 6.5, 5.0],
    'Ingles': [10.0, 6.0, 5.2, 4.3],
    'Quimica': [8.0, 10.0, 6.7, 7.0],
}
# DATAFRAME
notas_df = pd.DataFrame(dict_notas)
notas_df['Media'] = notas_df[['Matematica',
                              'Portugues', 'Ingles', 'Quimica']].mean(axis=1)

# EXIBINDO NOTAS
media = notas_df[notas_df.loc[:, 'Media'] < 7]
media_df = pd.DataFrame(media)
print(media)
