lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    cont = cont + 1
    if r in 'Nn':
        break
print(f'{cont} números foram digitados')
print(f'Os números digitados foram {lista}')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
