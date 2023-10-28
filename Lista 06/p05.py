'''Implemente uma calculadora com suas funções básicas: soma,
subtração, multiplicação e divisão. No programa principal, o usuário
deve informar dois números e escolher a operação que quer efetuar.
O programa chamará a função de acordo com a operação escolhida e
retornará o resultado.
A cada interação pergunte se o usuário deseja escolher uma nova
operação ou encerrar a execução.
Na operação de divisão, divida o maior número pelo menor.'''

import os
os.system("cls")


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


def divisao(n1, n2):
    if n1 > n2:
        return n1/n2
    else:
        return n2 / n1


operacao = input("Deseja realizar uma operação? [S] ou [N]: ").upper()

while operacao == "S":
    num1 = int(input("Digite o número 1: "))
    num2 = int(input("Digite o número 2: "))
    print(
        "Qual opção deseja realizar?\n [S] Soma\n [B] Subtração\n [M] Multiplicação\n [D] Divisão\n")
    opcao = input("Digite a operação desejada: ").upper()

    if opcao == "S":
        print(soma(num1, num2))
    elif opcao == "B":
        print(subtracao(num1, num2))
    elif opcao == "M":
        print(multiplicacao(num1, num2))
    elif opcao == "D":
        print(divisao(num1, num2))
    else:
        print("Opção inválida.")

    operacao = input("\nDeseja realizar outra operação? [S] ou [N]: ").upper()
