'''Crie um DataFrame que represente uma lista de Pokémon, incluindo as
seguintes colunas: "Nome", "Tipo". Em seguida, filtre o DataFrame para mostrar
apenas os Pokémon do tipo "Fogo". '''

import os
import pandas as pd

os.system("cls")

df_pokemon = pd.read_csv('pokemon.csv')
pokemons_fogo = df_pokemon[df_pokemon["Type 1"] == "Fire"]
print(pokemons_fogo)
