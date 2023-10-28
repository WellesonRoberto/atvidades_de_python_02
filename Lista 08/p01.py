

import pandas as pd

dados = {
      "Nome:": ["Well", "Daniel", "Nicolas"],
      "Cidade:": ["Recife", "João Pessoa", "Alagoas "],
      "Idade:":[27, 30, 25],
      "Contato:":["(81)88888888", "(83)99999999", "(85)77777777"]
}

df = pd.DataFrame(dados)
print(df)