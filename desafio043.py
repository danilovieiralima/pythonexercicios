peso = float(input('Qual é o seu peso?Kg '))
altura = float(input('Qual é a sua altura?M '))
imc = peso / (altura ** 2)
print('Calculando o seu IMC...')
print(f'O seu IMC é {imc:.1f}')
if imc < 18.50:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
