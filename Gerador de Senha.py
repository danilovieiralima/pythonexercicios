from random import sample

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '[]{}()*;/,._-'

juncao = (minusculas+maiusculas+numeros+simbolos)
tamanho = 16
senha = ''.join(sample(juncao, tamanho))
print(f'A senha é {senha}')
