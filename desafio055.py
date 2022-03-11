maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o {p} peso em KG:'))
    if p == 1:
        maior = peso
        menor = peso
    elif maior < peso:
        maior = peso
    elif menor > peso:
        menor = peso
print(f'O maior peso lido foi {maior}')
print(f'O menor peso lido foi {menor}')
