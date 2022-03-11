from time import sleep

c = ('\033[m',  # Cor 0 = Sem Cores
     '\033[0;30;41m',  # Cor 1 = Vermelho
     '\033[0;30;42m',  # Cor 2 = Verde
     '\033[0;30;43m',  # Cor 3 = Amarelo
     '\033[0;30;44m',  # Cor 4 = Azul
     '\033[0;30;45m',  # Cor 5 = Roxo
     '\033[0;30;47m',  # Cor 6 = Branco
     )


def escreva(texto, cor=0):
    tamanho = len(texto) + 4
    print(c[cor], end='')
    print('=' * tamanho)
    print(f'  {texto}')
    print('=' * tamanho)
    print(c[0], end='')


# Programa Principal
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    funcao = str(input('Função ou Biblioteca: ')).strip()
    if funcao.upper() in 'FIM':
        escreva('ATÉ LOGO!', 1)
        break
    escreva(f'Acessando o manual do comando [ {funcao} ]', 4)
    sleep(1)
    print(c[6], end='')
    help(funcao)
    print(c[0], end='')
