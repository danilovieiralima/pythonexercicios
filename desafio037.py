num = int(input('Digite um número qualquer: '))
conv = int(input(f'Você quer converter o número {num} para BINÁRIO(1), OCTAL(2) ou HEXADECIMAL(3): '))
if conv == 1:
    print('Convertendo o número para binário...')
    print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('Convertendo o número para octal...')
    print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('Convertendo o número para hexadecimal...')
    print('O número {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida! Digite uma opção válida.')
