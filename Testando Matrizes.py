'''somaimpar = coluna4 = 0
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-=' * 30)
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 != 0:
            somaimpar += matriz[l][c]
    print()
print(f'A soma de todos os valores ímpares é {somaimpar}')'''
matriz = [[0, 0], [0, 0], [0, 0]]
for l in range(0, 3):
    for c in range(0, 2):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 2):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
