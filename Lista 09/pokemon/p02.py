import os
import pandas as pd
os.system("cls")

df_pokemon = pd.read_csv('pokemon/pokemon.csv')

pokemon_filtrados = df_pokemon[(
    df_pokemon['Attack'] > 100) & (df_pokemon['Defense'] > 80)]

nomes_pokemon = pokemon_filtrados['Name']

print(nomes_pokemon)
