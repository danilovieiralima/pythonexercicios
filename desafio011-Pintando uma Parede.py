largura = float(input('A largura da parede é:'))
altura = float(input('A altura da parede é:'))
Area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(largura, altura, Area))
tinta = Area / 2
print('A quantidade de tinta necessária para pintar a parede é {} litros'.format(tinta))
