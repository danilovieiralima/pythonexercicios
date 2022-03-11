def maior(*numeros):
    maior = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f'Foram analisados {cont} valores.')
    print(f'O maior valor analisado foi {maior}')


maior(2, 4, 6, 8, 10)
maior(0, 10, 5)
maior(6, 2)
maior(8)
maior()
