# while True:
#    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#    if resp in 'SN':
#        break
# if resp == 'N':
#    break
pessoa = dict()
totalpessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F!')
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa['Idade']
    totalpessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 30)
print(totalpessoas)
print('-=' * 30)
print(f'A) Foram {len(totalpessoas)} pessoas cadastradas.')
media = soma / len(totalpessoas)
print(f'B) A média de idade do grupo é {media:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in totalpessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}, ', end='')
print()
print(f'D) A lista de pessoas com idade acima da média é:')
for p in totalpessoas:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f' {k}  =  {v} ', end='')
        print()
