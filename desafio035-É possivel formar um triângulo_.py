import math

a = float(input('Digite o comprimento da primeira reta:'))
b = float(input('Digite o comprimento da segunda reta:'))
c = float(input('Digite o comprimento da terceira reta:'))
print('O computador está analisando se é possível formar um triângulo...')
if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c or math.fabs(a - b) < c < a + b:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
