# COMANDOS PARA ADICIONAR OU SUBSTITUIR ELEMENTOS NA LISTA
'''lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picolé'
teste = 'Cookie'
print(lanche[3])
print(lanche)
lanche.append(teste)
print(lanche)
teste01 = 10.55
lanche.append(teste01)
print(lanche)
lanche.append(True)
print(lanche)
lanche.insert(0, 'Hot Dog')
print(lanche)
# COMANDOS PARA APAGAR ALGO DA LISTA
del lanche[3]
print(lanche)
lanche.pop(0)
print(lanche)
lanche.remove('Hambúrguer')
print(lanche)
del lanche[0:2]
print(lanche)
lanche.pop()
print(lanche)
if 'Cookie' in lanche:
    lanche.remove('Cookie')
print(lanche)'''
# COMO CRIAR UMA LISTA
# valores = list(range(4, 11))
# print(valores)
numeros = [8, 2, 5, 4, 9, 3, 0]
print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
# print(len(numeros))
'''num = [2, 5, 9, 1]
num.append(0)
num.insert(4, 8)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
'''valores = list()
for cont in range(1, 6):
    valores.append(int(input(f'Digite o valor {cont}:')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da Lista')'''
'''a = [2, 3, 4, 7]
b = a
b[2] = 8
a.remove(7)
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
'''a = [2, 3, 4, 7]
b = a[:]
b.remove(7)
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
