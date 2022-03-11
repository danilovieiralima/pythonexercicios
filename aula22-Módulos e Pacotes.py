"""MODULARIZAÇÃO:
   > Surgiu no ínicio dos anos 60
   > Sistemas ficando cada vez maiores
   > Foco: Dividir um programa grande, aumentar  a legibilidade,
   facilitar a manutenção.
"""


def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f = f * c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
