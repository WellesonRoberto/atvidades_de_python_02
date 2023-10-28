'''Faça uma função que retorne o reverso de um número
inteiro informado pelo usuário.
Por exemplo: 127 -> 721'''


def reverso(numero):
    # Vai converter o número para string, para ocorrer a inversão
    inumero = str(numero)
    return (numero[::-1])  # Inverte a ordem do número


numero = int(input("Digite um valor: "))
print(reverso(numero))
