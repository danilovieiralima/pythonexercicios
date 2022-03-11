def fatorial(numero, show=False):
    """
    --> Função que calcula o fatorial de um número
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número
    """
    from math import factorial
    if not show:
        return f'{factorial(numero)}'
    else:
        fat = 1
        for c in range(numero, 0, -1):
            print(c, end='')
            fat = fat * c
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        return fat

    # PROGRAMA PRINCIPAL


print(fatorial(5, show=False))
print(fatorial(5, show=True))
