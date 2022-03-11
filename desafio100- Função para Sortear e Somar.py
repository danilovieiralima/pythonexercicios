from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' '), sleep(0.5)
    print('Pronto!')


def somaPar(lista):
    print(f'A soma dos valores pares de {lista} é ', end='')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'{soma}', end='')


numeros = list()
sorteia(numeros)
somaPar(numeros)
