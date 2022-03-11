from random import randint
lista = list()
print('-' * 30)
print('   JOGA NA MEGA SENA   ')
print('-' * 30)
quant = int(input('Quantos jogos quer que eu sorteie? '))
cont = 0
while True:
    numero = randint(1, 60)
    if numero not in lista:
        lista.append(numero)
        cont = cont + 1
    if cont == 6:
        break
lista.sort()
print(f'Os números sorteados foram {lista}')
