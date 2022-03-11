print('GERADOR DE P.A')
print('=' * 30)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = termo1
cont = 1
while cont <= 10:
    print(f'{termo} > ', end='')
    termo = termo + razao
    cont = cont + 1
print(' FIM ')

