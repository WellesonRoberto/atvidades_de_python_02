'''Crie um DataFrame que represente jogos na steam, incluindo as seguintes
colunas: "Título do Jogo", "Plataforma", "Ano de Lançamento" e "Gênero". Em
seguida, filtre o DataFrame para mostrar apenas os jogos lançados após um ano
específico'''

import os
import pandas as pd

os.system("cls")

jogos = {
    'Titulo do Jogo': ['Stardew Valley', 'Pokémon Scarlet', 'Undertale'],
    'Plataforma': ['PC', 'Nintendo Switch', 'PC'],
    'Ano de Lancamento': [2010, 2022, 2013],
    'Gênero': ['Simulação', 'RPG', 'RPG']
}

df_jogos = pd.DataFrame(jogos)
jogos_2020 = df_jogos[df_jogos["Ano de Lancamento"] > 2020]
print(jogos_2020)
