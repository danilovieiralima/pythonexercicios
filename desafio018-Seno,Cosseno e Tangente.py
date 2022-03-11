import math
angulo = float(input('Qual é o valor do ângulo?'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O SENO de {angulo} é {seno:.2f}')
print(f'O COSSENO de {angulo} é {cosseno:.2f}')
print(f'A TANGENTE de {angulo} é {tangente:.2f}')
