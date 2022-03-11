distancia = float(input('Quantos Km irá percorrer na sua viagem?'))
if distancia <= 200.00:
    preco1 = distancia * 0.50
    print(f'O preço da sua passagem é R${preco1:.2f}')
else:
    preco2 = distancia * 0.45
    print(f'O preço da sua passagem é R${preco2:.2f}')
