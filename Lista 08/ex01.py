'''Crie um DataFrame representando as despesas mensais de uma pessoa, com as
seguintes colunas: "Mês", "Aluguel", "Alimentação". Calcule a despesa total de
cada mês (soma das colunas "Aluguel" e “Alimentação") e adicione essa
informação como uma nova coluna chamada "Despesa Total".'''

import os
import pandas as pd

os.system("cls")

despesas = {
    "Mes ": ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho"],
    "Aluguel": [800, 800, 800, 800, 800, 800],
    "Alimentacao": [700, 720, 800, 750, 790, 850]
}

df_despesas = pd.DataFrame(despesas)

df_despesas["Despesa total"] = df_despesas["Aluguel"] + \
    df_despesas["Alimentacao"]

print(df_despesas)
