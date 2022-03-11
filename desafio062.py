print('GERADOR DE P.A')
print('=' * 30)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = termo1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo = termo + razao
        cont = cont + 1
    print(' PAUSA ')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'O total de termos mostrados foi {total}')
print(' FIM ')
