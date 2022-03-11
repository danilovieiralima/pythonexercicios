def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!Digite um valor inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o valor\033[m')
            return 0
        else:
            return numero


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!Digite um valor inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar o valor\033[m')
            return 0
        else:
            return numero


# Programa Principal
num1 = leiaInt('Digite um valor inteiro:')
num2 = leiaFloat('Digite um valor real:')
print(f'O valor inteiro digitado foi {num1} e o valor real foi {num2}')
