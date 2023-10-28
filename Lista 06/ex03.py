'''Desenvolva um programa que tenha uma função chamada auxilio() que irá
receber como parâmetro o ano de nascimento de uma pessoa, retornando
como resultado se uma pessoa terá ou não direito ao auxilio escolar:
Autorizado: entre 4 (incluso) e 16 anos (incluso);
Negado: menos de 4 anos e maior que 16.'''

import os
os.system("cls")


def auxilo(ano):
    idade = 2023 - ano

    if 4 <= idade <= 16:
        return "Auxílio autorizado"
    else:
        return "Auxílio negado."


ano = int(input("Digite o ano de nascimento: "))

resultado = auxilo(ano)
print(f"Status do auxílio: {resultado}")
