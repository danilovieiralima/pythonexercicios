'''  def linha():
    print('-' * 30)


# PROGRAMA PRINCIPAL
linha()
print('     CURSO EM VÍDEO     ')
print('     APRENDA PYTHON     ')
print('     GUSTAVO GUANABARA  ')
linha()

print('-' * 30)
print('    SISTEMA DE ALUNOS    ')
print('-' * 30)
print('-' * 30)
print('    CADASTRO DE FUNCIONÁRIOS    ')
print('-' * 30)
print('-' * 30)
print('    ERRO DO SISTEMA    ')
print('-' * 30)


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('DANILO')
mensagem('DANIEL')


# DEFININDO A FUNÇÃO:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# CHAMANDO A FUNÇÃO(PROGRAMA PRINCIPAL):
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=2, b=10)
soma(b=2, a=10)


def contador(*num):
    tamanho = len(num)
    print(f'Recebi {tamanho} números e eles são {num}')


contador(1, 2)
contador(5, 4, 3, 2, 1)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos = pos + 1


valores = [2, 4, 6, 8, 10]
dobra(valores)
print(valores)'''
