'''Desenvolva uma função que permita receber uma variável
inteira X inúmeras vezes (deve parar quando o valor digitado for igual a
zero). Como retorno da função, para cada valor lido deverá ser imprimido a
sequência de 1 até X (o número digitado), com um espaço entre cada
número e seu sucessor.'''

import os
os.system("cls")


def imprimir_sequencia(x):
    if x <= 0:
        print("Programa encerrado.")
        return
    for i in range(1, x + 1):
        print(i, end=" ")
    print()
    novo_x = int(input("Digite um novo valor inteiro (ou 0 para sair): "))
    imprimir_sequencia(novo_x)


# Chame a função inicialmente com um valor
valor_inicial = int(input("Digite um valor inteiro (ou 0 para sair): "))
imprimir_sequencia(valor_inicial)
