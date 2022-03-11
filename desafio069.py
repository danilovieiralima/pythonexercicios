total18 = 0
totalhomens = 0
totmulher20 = 0
r = 'S'
while r == 'S':
    print('CADASTRE UMA PESSOA')
    sexo = str(input('Digite o seu sexo [M/F]:')).strip().upper()[0]
    idade = int(input('Digite a sua idade:'))
    r = str(input('Quer continuar? [S/N]')).strip().upper()
    if sexo in 'Mm':
        totalhomens = totalhomens + 1
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
    if sexo in 'MmFf' and idade > 18:
        total18 = total18 + 1
print(f'Há {totalhomens} homens cadastrados')
print(f'Há {totmulher20} mulheres com menos de 20 anos cadastradas')
print(f'Há {total18} pessoas com mais de 18 anos cadastradas')
print('FIM')
