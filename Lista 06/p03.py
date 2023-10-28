'''Faça uma função que calcule a média de um aluno (duas
notas) de acordo com o critério definido neste curso.
Além disso, faça uma segunda função que informe o status
do aluno de acordo com a tabela a seguir:
Nota acima de 6: “Aprovado”
Nota entre 4 e 6: “Verificação Suplementar”
Nota abaixo de 4: “Reprovado”
Utilizar duas funções'''


def media(nota1, nota2):
    media = (nota1+nota2)/2
    return media


def media_final(media):
    if media > 6:
        print(f"Aprovado com média {media}")
    elif media >= 4 or media <= 6:
        print(f"Verificação suplementar. Você ficou com a média {media}")
    else:
        print(f"Reprovado.. Você ficou com a média {media}")


nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = media(nota1, nota2)
media_final(media)
