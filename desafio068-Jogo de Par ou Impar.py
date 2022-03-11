from random import randint
cont = 0
print('=' * 30)
print('JOGO DE PAR OU ÍMPAR')
print('=' * 30)
computador = randint(0, 10)
while True:
    jogador = int(input('Diga um valor: '))
    par = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if par == 'P':
        if (jogador + computador) % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}.Total de {jogador + computador}. Deu PAR!')
            print('Você venceu!Vamos outra vez!')
        elif(jogador + computador) % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}.Total de {jogador + computador}. Deu ÍMPAR')
            print('Você perdeu!')
            break
        cont = cont + 1
    if par == 'I':
        if (jogador + computador) % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}.Total de {jogador + computador}. Deu PAR')
            print('Você perdeu!')
            break
        elif(jogador + computador) % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}.Total de {jogador + computador}. Deu ÍMPAR')
            print('Você venceu!Vamos outra vez!')
        cont = cont + 1
print(f'Você venceu {cont} vezes')
print('FIM')
