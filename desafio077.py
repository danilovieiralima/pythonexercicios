palavras = ('APRENDER', 'PROGRAMAR', 'ESTUDAR', 'ANDAR',
            'CORRER', 'BATER', 'MORRER', 'VIVER', 'SOFRER', 'PULAR', 'SALTAR')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letras in p:
        if letras in 'AEIOU':
            print(letras, end=' ')

