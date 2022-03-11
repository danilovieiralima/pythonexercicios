from time import sleep
a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
opcao = 0
while opcao != 5:
    opcao = int(input('''Essas são suas opções:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA\n'''))
    if opcao == 1:
        print(f'O resultado da soma de {a} + {b} é {a + b}')
    elif opcao == 2:
        print(f'O resultado da multiplicação de {a} x {b} é {a * b}')
    elif opcao == 3:
        if a > b:
            print(f'O maior número entre {a} e {b } é {a}')
        if b > a:
            print(f'O maior número entre {a} e {b} é {b}')
        if a == b:
            print('Não há número maior, os 2 tem o mesmo valor')
    elif opcao == 4:
        a = int(input('Escolha um novo número:'))
        b = int(input('Escolha um outro novo número:'))
    elif opcao == 5:
        print('Saindo do programa... '), sleep(1)
        print('O programa foi ENCERRADO')
    else:
        print('Opção Inválida. Digite novamente')
print('===================FIM==========================')