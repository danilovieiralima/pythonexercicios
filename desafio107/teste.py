import moeda
p = float(input('Digite o preço:R$'))
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'Aumentando 10% de R${p}, temos R${moeda.aumentar(p, 10)}')
