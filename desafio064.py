n = s = cont = 0
n = int(input('Digite um número: '))
while n != 999:
    cont = cont + 1
    s = s + n
    n = int(input('Digite um número: '))
print(f'Você digitou {cont} números')
print(f'A soma dos números é {s}')
