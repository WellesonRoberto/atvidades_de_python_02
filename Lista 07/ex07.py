'''Crie um programa que utilize o Broadcasting do NumPy para calcular a média de
despesas de uma empresa, para cada mês e identificar os meses em que as
despesas foram superiores ao dobro da média anual. '''

import numpy as np

# Suponhamos que você tem um array 2D onde as linhas representam meses e as colunas representam os anos.
# Cada elemento do array representa as despesas de uma empresa para um mês específico.

despesas = np.array([
    [1000, 1200, 800, 950],  # Janeiro
    [1100, 1300, 850, 1000],  # Fevereiro
    [1200, 1400, 900, 1050],  # Março
    [1050, 1250, 820, 970],   # Abril
    [2000, 1100, 900, 1200],  # Maio
    [1500, 1450, 1600, 1100],  # Junho
    [2000, 2300, 3000, 3400],  # Julho
    [1500, 1400, 1400, 1300],  # Agosto
    [1200, 1100, 1205, 1210],  # Setembro
    [1350, 1220, 1100, 1000],  # Outubro
    [1400, 2000, 1500, 3000],  # Novembro
    [3000, 3200, 2900, 5000]  # Dezembro
])

# Calculando a média anual (soma das despesas de todos os meses dividida pelo número de meses)
media_anual = np.mean(despesas, axis=0)

# Usando broadcasting para verificar quais meses tiveram despesas superiores ao dobro da média anual
meses_acima_da_media_anual = despesas > (2 * media_anual)

# Obtendo os meses onde as despesas foram superiores ao dobro da média anual
meses_acima_da_media_anual_indices = np.where(meses_acima_da_media_anual)

# Mostrando os resultados
for mes, ano in zip(*meses_acima_da_media_anual_indices):
    print(
        f"Despesas do {mes+1}º mês no ano {ano+1} foram superiores ao dobro da média anual.")
