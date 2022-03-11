n = cont = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont = cont + 1
    s = s + n
print(f'São {cont} números e a soma deles é {s}')
print('FIM')
