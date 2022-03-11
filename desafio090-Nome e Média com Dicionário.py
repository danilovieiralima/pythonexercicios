dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
print('-=' * 30)
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
elif dados['Média'] < 5:
    dados['Situação'] = 'Reprovado'
elif 7 > dados['Média'] >= 5:
    dados['Situação'] = 'Recuperação'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
