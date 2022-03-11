# boletim = [nome, [nota1, nota2], media]
boletim = []
cont = 0
while True:
    cont += 1
    print(f'{cont}°ALUNO')
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>15}')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>15.1f}')
print('-=' * 30)
while True:
    opc = int(input('Quer mostrar as notas de qual aluno?[999 interrompe]'))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'As notas de {boletim[opc][0]} são {boletim[opc][1]}')
