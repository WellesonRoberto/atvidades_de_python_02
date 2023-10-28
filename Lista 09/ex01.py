'''Idade e Gênero
No DataFrame df_dados_vacinacao, selecione todas as entradas de pessoas
com idade maior que 60 anos (idade > 60) do gênero feminino. '''

import pandas as pd

import os
os.system("cls")

df_dados_vacinacao = pd.read_csv("Lista 09/vacinados.csv")
feminino_maior_60 = df_dados_vacinacao[(df_dados_vacinacao["idade"] > 60) & (
    df_dados_vacinacao["sexo"] == "FEMININO")]
print(feminino_maior_60[["idade", "sexo"]])
print()

'''Ordenação pela data
Ordene o DataFrame df_dados_vacinacao com base na coluna "data_vacinacao"
em ordem decrescente. Exiba as 10 primeiras entradas. '''

print(df_dados_vacinacao.tail(10)[["data_vacinacao"]])
print()

'''Fabricante de Vacina
No DataFrame df_dados_vacinacao filtre as pessoas com faixa etária entre 25 a
29 anos da cor parda e preta que moram em Recife que tomaram a vacina
PFIZER. '''

pfizer = df_dados_vacinacao[(
    df_dados_vacinacao["faixa_etaria"] == "25 a 29 anos") & (df_dados_vacinacao["raca_cor"] == "PRETA") & (df_dados_vacinacao["municipio"] == "RECIFE") & (df_dados_vacinacao["vacina_fabricante"] == "3 - COMIRNATY (PFIZER)")]
print(pfizer[["faixa_etaria", "raca_cor", "municipio", "vacina_fabricante"]])

'''Exportar Dados
Exporte o DataFrame df_dados_vacinacao para um novo arquivo CSV chamado
"dados_vacinacao_filtrados.csv", incluindo apenas as colunas: "faixa_etaria",
"idade", "sexo", "raca_cor", "municipio" e "data_vacinacao". '''

arquivo_vacinacao = open(
    "df_dados_vacinacao_filtrados.csv", "w", encoding="utf8")
dados = df_dados_vacinacao[["faixa_etaria",
                            "idade", "sexo", "raca_cor", "municipio", "data_vacinacao"]]
dados.to_csv("df_dados_vacinacao_filtrados.csv", index=False)
