s = 0
cont = 0
for c in range(1, 7):
    if c % 2 == 0:
        s = s + c
        cont = cont + 1
print(f'Você digitou {cont} PARES e a soma deles é {s}')
