def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if formatado is False else moeda(res)


def metade(preco=0, formatado=False):
    res = preco / 2
    return res if formatado is False else moeda(res)


def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def resumo(preco=0, taxaaumento=10, taxareducao=5):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preco, taxaaumento, True)}')
    print(f'{taxareducao}% de redução: \t\t{diminuir(preco, taxareducao, True)}')


def moeda(preco=0, moeda='R$', formatado=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
