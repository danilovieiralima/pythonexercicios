lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 != 0:
        lista[1].append(n)
lista[0].sort()
print(f'Os valores pares em ordem crescente são {lista[0]} ')
lista[1].sort()
print(f'Os valores ímpares em ordem crescente são {lista[1]}')
