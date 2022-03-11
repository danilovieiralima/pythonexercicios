import math
catetooposto = float(input('Qual a medida do cateto oposto?'))
catetoadjacente = float(input('Qual a medida do cateto adjacente?'))
print(f'A medida da hipotenusa é {math.hypot(catetooposto, catetoadjacente):.2f}')

'''from math import sqrt
co = float(input('Qual a medida do cateto oposto?'))
ca = float(input('Qual a medida do cateto adjacente?'))
hi = sqrt(co ** 2 + ca ** 2 )
print(f'A medida da hipotenusa é: {hi:.2f}')'''
