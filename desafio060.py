'''import math
n = int(input('Digite um número:'))
fatorial = math.factorial(n)
print(f'{n}! é {fatorial}')'''
'''n = int(input('Digite um número:'))
resultado = 1
for n in range(1, n + 1):
    resultado = resultado * n
print(f'O fatorial de {n} é {resultado}')'''
n = int(input('Digite um número:'))
c = n
f = 1
while c > 0:
    f = f * c
    c = c - 1
print(f'Calculando {n}!...')
print(f'O fatorial de {n} é {f}')
