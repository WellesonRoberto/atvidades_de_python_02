'''Crie uma nova coluna chamada "Combined_Types" no
DataFrame df_pokemon que contenha a
concatenação dos tipos primário (type 1) e secundário
(type 2) de cada Pokémon, separados por um traço
("-"). Por exemplo, se um Pokémon tem o tipo primário
"Fire" e o tipo secundário "Flying", a nova coluna deve
conter "Fire-Flying". Exiba as últimas 5 linhas do
DataFrame com a nova coluna e o nome dos
pokémons.'''


import pandas as pd
import os

os.system("cls")

df_pokemon = pd.read_csv("pokemon/pokemon.csv")

df_pokemon["Combined_Types"] = df_pokemon["Name"] + \
    df_pokemon["Type 1"] + "-" + df_pokemon["Type 2"]
df_pokemon = df_pokemon[["Name", 'Combined_Types']]
print(df_pokemon.tail(5))

# exportando arquivo csv
# df_pokemon.to_csv("pokemon/pokemon.csv")

# exporanto arquivo csv sem index
# df_pokemon.to_csv("pokemon/pokemon.csv")
