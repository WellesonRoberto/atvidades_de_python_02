'''Faça um programa que tenha uma lista(vetor) chamada números e
duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números (entre 0 e 99) e vai
colocá-los dentro da lista.
E a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.'''

# randint(a, b) : retorna um número inteiro aleatório no intervalo entre a e b
from random import randint
import os
os.system("cls")


def sorteia():
    numeros = []
    for i in range(5):  # Irá sortear 5 números
        numeros.append(randint(0, 99))  # No intervalo de 0 e 99
    print(f"\nSorteando {len(numeros)} valores da lista.")

    for i in numeros:
        print(f"{i}", end=" ")
    return numeros


def somar_par(lista_numeros):
    pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            pares.append(i)
    print(f"\nOs valores pares da lista são {pares}")
    print(f"\nA soma dos pares é: {sum(pares)}")


somar_par(sorteia())
