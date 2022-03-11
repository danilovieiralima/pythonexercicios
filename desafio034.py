salario = float(input('Qual é o seu salário?R$ '))
if salario > 1250:
    aumento = (salario * 10 / 100) + salario
    print(f'Você recebeu um aumento de 10%. Seu novo salário é R${aumento:.2f}')
if salario <= 1250:
    aumento = (salario * 15 / 100) + salario
    print(f'Você recebeu um aumento de 15%. Seu novo salário é R${aumento:.2f}')
