import random
print('O computador está escolhendo  um número de 0 a 5...')
num = random.randint(0, 5)
usuario = int(input('Qual número o computador escolheu?'))
if usuario == num:
    print('Você acertou!')
    print(f'O número que o computador escolheu foi {num}!')
else:
    print('Você errou!')
    print(f'O número que o computador escolheu foi {num}')

print('===FIM===')
