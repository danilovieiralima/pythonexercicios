listatotal = []
while True:
    n = int(input('Digite um número:'))
    if n not in listatotal:
        listatotal.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    r = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Os valores digitados foram {listatotal}')
