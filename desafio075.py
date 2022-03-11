valores = (int(input('Digite um número:')),
           int(input('Digite outro número:')),
           int(input('Digite mais outro número:')),
           int(input('Digite o último número:')),)
print(f'Os valores digitados foram {valores} ', end='')
print(f'\nO valor 9 apareceu {valores.count(9)} vezes')
if 3 not in valores:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O primeiro valor 3 está na {valores.index(3) + 1} posição')
print('Os valores pares digitados foram ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
