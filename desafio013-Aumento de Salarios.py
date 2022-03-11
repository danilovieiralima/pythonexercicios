salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15/100)
print('O novo salário do funcionário com 15% de aumento é R${:.2f}'.format(novo))
