lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número:')))
    r = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if r != 'S':
        break
print(f'A lista completa é {lista}')
for p in lista:
    if p % 2 == 0:
        par.append(p)
for i in lista:
    if i % 2 != 0:
        impar.append(i)
print(f'A lista somente com pares é {par}')
print(f'A lista somente com ímpares é {impar} ')
