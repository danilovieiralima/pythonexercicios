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


def linha(tam=42):
    return '=' * tam


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m- \033[34m{item}\033[m')
        cont = cont + 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção:\033[m ')
    return opcao
