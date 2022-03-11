def dobro(preco=0):
    preco2 = preco * 2
    return preco2


def metade(preco=0):
    preco2 = preco / 2
    return preco2


def aumentar(preco=0, taxa=0):
    preco2 = preco + (preco * taxa / 100)
    return preco2


def diminuir(preco=0, taxa=0):
    preco2 = preco - (preco * taxa / 100)
    return preco2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
