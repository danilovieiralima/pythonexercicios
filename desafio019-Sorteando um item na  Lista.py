from random import choice
n1 = str(input('Qual é o nome do primeiro aluno? '))
n2 = str(input('Qual é o nome do segundo aluno? '))
n3 = str(input('Qual é o nome do terceiro aluno? '))
n4 = str(input('Qual é o nome do quarto aluno? '))
lista = [n1, n2, n3, n4]
choice(lista)
print(f'O aluno escolhido para apagar o quadro é {choice(lista)}')
