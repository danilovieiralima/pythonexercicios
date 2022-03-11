reais = float(input('Quanto dinheiro vc tem na carteira? R$'))
dolar = reais / 3.27
print('Com R${:.2f} vc pode comprar US${:.2f}'.format(reais, dolar))
