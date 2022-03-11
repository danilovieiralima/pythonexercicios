'''try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except Exception as erro:
    print(f'ERRO!O problema foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')'''

try:
    a = int(input('Numerador:'))
    b = int(input('Denominador:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário não quis digitar os dados')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
