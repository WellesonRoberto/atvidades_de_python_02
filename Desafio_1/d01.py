'''Desenvolva um programa em Python que apure o resultado de uma votação para determinar o 
personagem favorito do desenho “The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:

1 - Bart
2 - Homer
 
Considere que existe uma função que recebe e escreve em um arquivo .txt ou em uma lista/vetor
os votos de 5 pessoas. Um voto é representado pelo código de identificação do candidato.

Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, 
como resultado:

- o nome e a quantidade de votos do candidato mais votado
- o nome e a quantidade de votos do menos votado
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2).'''

import os
os.system("cls")


def votacao():
    votos = []
    bart = []
    homer = []
    nulos = []
    for i in range(5):
        voto = input(
            "Digite seu voto:\n1 - Bart \n2 - Homer\n0 - Nulo\n Voto: ")
        votos.append(voto)

    with open("Desafio_1/arquivo.txt", "w") as arquivo:
        for voto in votos:
            arquivo.write(voto + "\n")

    arquivo.close()


def resultado():
    votos_bart = 0
    votos_homer = 0
    votos_nulos = 0

    with open("Desafio_1/arquivo.txt", "r") as arquivo:
        for votos in arquivo:
            votos = int(votos)
            if votos == 1:
                votos_bart += 1
            elif votos == 2:
                votos_homer += 1
            else:
                votos_nulos += 1

        if votos_bart > votos_homer:
            print(
                f"\nResultado dos votos:\n\nO personagem favorito do The Simpsons é o Bart com {votos_bart} votos. O menos votado foi o Homer com {votos_homer} voto(s). Tiveram {votos_nulos} nulo(s).")
        elif votos_bart < votos_homer:
            print(
                f"\nResultado dos votos:\n\nO personagem favorito do The Simpsons é o Homer com {votos_homer} votos. O menos votado foi o Bart com {votos_bart} voto(s). Tiveram {votos_nulos} nulo(s).")
        elif votos_bart == votos_homer:
            print(
                f"\nResultado dos votos:\n\nOs personagens do The Simpsons Homer e Bart ficaram empatados, com {votos_bart} votos cada. Tiveram {votos_nulos} nulo(s).")
            print()


votacao()
resultado()
