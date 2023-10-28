import pandas as pd

estados_nordeste = [["Alagoas", "AL", "3,4 milhões", "Maceió"],
                    ["Bahia", "BA", "15,4 milhões", "Salvador"],
                    ["Ceará", "CE", "9,2 milhões", "Fortaleza"],
                    ['Maranhão', 'MA', '7,1 milhões', 'São luiz'],
                    ['Paraiba', 'PB', '4.0 milhões', 'João Pessoa'],
                    ['Pernambuco', 'PE', '3,4 milhões', 'Recife'],
                    ['Piauí', 'PI', '3,3 milhões', 'Teresina'],
                    ['Rio Grande do Norte', 'RN', '3,5 milhões', 'Natal'],
                    ['Sergipe', 'SE', '2,4 milhões', 'Aracaju']]


df = pd.DataFrame(estados_nordeste, columns=["Estado", "Sigla", "População", "Capital"])
idh = [0.631, 0.631, 0.692, 0.631, 0.631, 0.692, 0.631, 0.631, 0.692]
df["IDH"] = idh
print(df)
print()
print(df.loc[0])
print()
print(df.loc[2:4, ["Estado", "Sigla"]])
print()
print(df.iloc[1:4, 0:3])