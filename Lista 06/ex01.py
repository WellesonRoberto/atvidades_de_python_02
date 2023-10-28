'''Faça um programa que receba um valor em horas e dê duas opções ao
usuário, converter em minutos ou em segundos. A partir da escolha do
usuário, o programa deverá chamar a função específica de conversão. A
função para converter horas em minutos deverá receber como parâmetro a
hora e retornar o valor em minutos. A função para converter horas em
segundos deverá receber como parâmetro a hora e retornar o valor em
segundos. Por fim, o programa principal imprime o valor retornado pela
função.'''

import os
os.system("cls")


def minutos(hora):
    min = horas * 60
    return min


def segundos(hora):
    seg = horas * 3600
    return seg


horas = int(input("Digite a hora para conversão: "))
opcao = input(
    "Digite a opção da conversão: [M] Minutos ou [S] Segundos? ").upper()

if opcao == "M":
    print(
        f" Covertentedo {horas} horas em minutos: {(minutos(horas))} minutos.")

elif opcao == "S":
    print(
        f" Covertentedo {horas} horas em seguntos: {(segundos(horas))} segundos.")
else:
    print("Opção inválida!")
