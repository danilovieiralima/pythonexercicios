'''cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont = cont + 1
print('ACABOU')'''
'''cont = 1
while True:
    print(cont, '->', end='')
    cont = cont + 1'''
'''n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont = cont + 1
print('ACABOU')'''
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s = s + n
print(f'A soma dos números é {s}')
