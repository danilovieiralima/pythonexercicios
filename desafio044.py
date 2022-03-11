preconormal = float(input('Qual o valor da compra?R$ '))
print('''Suas opções de pagamento são:
[1] Á vista dinheiro/cheque:10% de desconto
[2] Á vista no Cartão:5% de desconto
[3] Em até 2x no Cartão:Preço normal
[4] Em até 3x ou mais no Cartão:20% de juros
''')
pagamento = int(input('Qual a opção de pagamento? '))
if pagamento == 1:
    novopreco = preconormal - (preconormal * 10 / 100)
    print(f'O valor final da compra á vista em dinheiro/cheque com 10% de desconto é R${novopreco:.2f}')
elif pagamento == 2:
    novopreco = preconormal - (preconormal * 5 / 100)
    print(f'O valor final á vista no Cartão com 5% de desconto é R${novopreco:.2f}')
elif pagamento == 3:
     novopreco = print(f'O valor final da compra são 2x de R${preconormal/2} SEM JUROS')
elif pagamento == 4:
    total = preconormal + (preconormal * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de R${preconormal:.2f} vai custar R${total:.2f} no final')

