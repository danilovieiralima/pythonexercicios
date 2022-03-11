# sexo = str(input('Diga seu sexo:'))
# correto = sexo == 'm' or sexo == 'f'

# while not correto:
#    print('Digite novamente')
#    sexo = str(input('Diga seu sexo:'))
#    correto = sexo == 'm' or sexo == 'f'
# print('Obrigado')
sexo = str(input('Digite o seu sexo:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite o seu sexo:')).strip().upper()[0]
print(f'Sexo {sexo} informado com sucesso')