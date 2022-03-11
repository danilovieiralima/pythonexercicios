preco = float(input('Qual o preço do produto? R$'))
novopreco = preco - (preco * 5/100)
print('O  preço do produto com desconto de 5% é R${:.2f}'.format(novopreco))
