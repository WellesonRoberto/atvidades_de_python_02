import pandas as pd

df_pokemon = pd.read_csv("pokemon/pokemon.csv")
df_pokemon = df_pokemon.sort_values(["Type 1", "Name"])
# head(10) = visualiza as 10 primeiras linhas do DataFrame
print(df_pokemon.head(10)[["Name", "Type 1"]])
print()
# tail(5) = visualiza as 8 ultimas linhas do DataFrame
print(df_pokemon.tail(8)[["Name", "Type 1"]])
print()
# Vizualinza as colunas
print(df_pokemon.columns)
print()
# Vizualiza as informações da linha
print(df_pokemon.index)
print()
# Vizualiza informações sobre o DataFrame
print(df_pokemon.info())
print()
# Filtra pokemons legendários
print(df_pokemon.loc[df_pokemon["Legendary"] == True])
print()
