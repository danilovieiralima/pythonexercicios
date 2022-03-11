casa = float(input('Qual é o preço da casa?R$ '))
salario = float(input('Qual  é o salário do comprador?R$ '))
tempo = int(input('Em quantos anos irá pagar a casa? '))
qprestacao = int(tempo * 12)
valorprestacao = casa / (tempo * 12)
print('Analisando o seu caso...')
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${valorprestacao:.2f}')
if valorprestacao > (salario * 30/100):
    print('Seu empréstimo foi NEGADO')
elif valorprestacao <= (salario * 30/100):
    print('Seu empréstimo foi APROVADO')
