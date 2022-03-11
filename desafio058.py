from random import randint
computador = randint(0, 10)
print('O computador está escolhendo um número de 0 a 10...')
cont = 0
acertou = False
while not acertou:
    cont = cont + 1
    jogador = int(input('Qual número o computador escolheu?'))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente outra vez!')
        elif jogador > computador:
            print('Menos...Tente outra vez!')
print(f'Acertou com {cont} tentativas')


