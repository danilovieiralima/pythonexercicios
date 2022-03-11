r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO')
    elif r1 != r2 != r3:
        print('O triângulo formado é ESCALENO')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('O triângulo formado é ISÓSCELES')
else:
    print('Não é possível formar um triângulo')
