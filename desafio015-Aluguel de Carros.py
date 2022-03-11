dias = float(input('O carro foi alugado por quantos dias?'))
distancia = float(input('Quantos Km o carro percorreu?'))
custototal = (dias * 60) + (distancia * 0.15)
print(f'O preço a pagar por o aluguel do carro é R${custototal:.2f}')
