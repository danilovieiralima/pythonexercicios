# texto = 'Meu nome é Danilo Vieira'
# texto2 = texto[::-1]
# print(f'O texto {texto} invertido é {texto2}')


def inverter(msg):
    return msg[::-1]


texto = str(input('Digite um texto qualquer: ')).strip().upper()

print(f'O texto invertido é {inverter(texto)}')
