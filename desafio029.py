velocidade = int(input('Qual a velocidade do carro? Km/h '))
if velocidade > 80:
    print('Você ultrapassou o limite na pista e foi multado ')
    multa = 7 * (velocidade - 80)
    print(f'O valor da sua multa é de R${multa}')
else:
    print('Você está dirigindo dentro dos limites. Parabéns! ')
