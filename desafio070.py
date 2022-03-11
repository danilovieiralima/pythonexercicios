print('=' * 30)
print('LOJA DE COMPRAS')
print('=' * 30)
r = 'S'
cont = 0
totalpreco = 0
maisde1000 = 0
menorpreco = 0
nome_produto_barato = ''
while r == 'S':
    print('CADASTRE UM PRODUTO')
    nome = str(input('Digite o nome do seu produto:')).strip()
    preco = int(input('Digite o valor do seu produto:R$'))
    r = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    cont = cont + 1
    totalpreco = totalpreco + preco
    if preco > 1000:
        maisde1000 = maisde1000 + 1
    if cont == 1:
        menorpreco = preco
        nome_produto_barato = nome
    else:
        if preco < menorpreco:
            menorpreco = preco
            nome_produto_barato = nome
print(f'O valor total das compras foi de R${totalpreco}')
print(f'Há {maisde1000} produtos que custam mais de R$1000')
print(f'O valor do produto mais barato é R${menorpreco} e seu nome é {nome_produto_barato}')
print('FIM DAS COMPRAS')