print('=' * 30)
print('PROGRAMA TABUADA')
print('=' * 30)
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c:2} = {n * c}')
    elif n < 0:
        break
print('FIM DO PROGRAMA')
