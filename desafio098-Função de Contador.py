from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        abs(passo)
    if passo == 0:
        passo = 1

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=''), sleep(0.5)
            cont = cont + passo
        print('FIM!')
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end=''), sleep(0.5)
            cont = cont - passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
