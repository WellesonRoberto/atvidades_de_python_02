'''Desenvolva um programa que tenha uma função que escreva em um arquivo
um conjunto de 6 nomes (1 por linha). O programa principal deverá ordenar
os nomes e gerar um novo arquivo com os nomes ordenados.'''

# Função para escrever nomes em um arquivo


def escrever_nomes_em_arquivo():
    nomes = []
    for i in range(6):
        nome = input("Digite o nome: ")
        nomes.append(nome)

    with open("nomes.txt", "w") as arquivo:
        for nome in nomes:
            arquivo.write(nome + "\n")

# Função para ler, ordenar e escrever os nomes ordenados em um novo arquivo


def ordenar_e_escrever_nomes():
    with open("nomes.txt", "r") as arquivo:
        nomes = [linha.strip() for linha in arquivo]

    nomes.sort()

    with open("nomes_ordenados.txt", "w") as arquivo_ordenado:
        for nome in nomes:
            arquivo_ordenado.write(nome + "\n")


# Chamando a função para escrever os nomes no arquivo
escrever_nomes_em_arquivo()

# Chamando a função para ordenar e escrever os nomes ordenados em um novo arquivo
ordenar_e_escrever_nomes()
