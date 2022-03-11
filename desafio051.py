termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo1 + (10-1) * razao
for c in range(termo1, decimo + razao, razao):
    print(c)
print('ACABOU')
