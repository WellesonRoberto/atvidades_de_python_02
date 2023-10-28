'''Crie um DataFrame com os seguintes dados:

● Produto: Smartphone, Laptop, Tablet, Fone de Ouvido, Smart TV
● Quantidade Vendida: 100, 50, 80, 120, 30
● Preço Unitário (em reais): 800, 2500, 600, 80, 1800
● Calcule a receita total para cada produto (quantidade vendida multiplicada pelo preço unitário) e
adicione essa informação como uma nova coluna chamada "Receita".
● Selecione apenas os produtos que tiveram uma quantidade vendida superior a 80 unidades.'''

import pandas as pd

produtos = {
    "Nome:": ["Smartphone", "Laptop", "Tablet", "Fone de ouvido", "Smart TV"],
    "Quantidade_vendida": [100, 50, 80, 120, 30],
    "Preco_unitario": [800, 2500, 600, 80, 1800]
}

df_produtos = pd.DataFrame(produtos)


df_produtos["Receita(em reias)"] = df_produtos["Quantidade_vendida"] * \
    df_produtos["Preco_unitario"]

df_produtos_mais_vendidos = df_produtos[df_produtos["Quantidade_vendida"] > 80]
print(df_produtos_mais_vendidos)
