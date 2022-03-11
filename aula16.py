''' TUPLAS SÃO IMUTÁVEIS
lanche = () --> TUPLAS
lanche = []  --> DICIONÁRIOS
lanche = {} --> LISTAS'''
'''print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-1])
print(lanche[-4])
print(lanche[1:])
print(lanche[0:3])
print(lanche[:2])
print(lanche[:])
print(lanche[::])'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
 for comida in lanche:
 print(f'Eu vou comer {comida}')
 print(len(lanche))
 for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
 for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(sorted(lanche))
# print(lanche)
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
# print(len(c))
# print(c.count(5))
# print(c.index(8))
print(c.index(5) + 1)
pessoa = ('Gustavo', 39, 'M', 99.8)
del(pessoa)
print(pessoa)'''
