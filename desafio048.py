soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A quantidade de números é {cont} e a soma deles é {soma}')
