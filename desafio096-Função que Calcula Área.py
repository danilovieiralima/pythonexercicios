def area(largura, comprimento):
    a = l * c
    print(f'A área de um terreno de {largura}x{comprimento} é de {a:.2f}m2')


# PROGRAMA PRINCIPAL
print('CONTROLE DE TERRENOS')
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)
