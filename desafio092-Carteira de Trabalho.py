# No programa, a pessoa vai se aposentar após 35 anos de contribuição.
from datetime import date
carteira = dict()
carteira['Nome'] = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de Nascimento: '))
carteira['Idade'] = date.today().year - ano_de_nascimento
carteira['CTPS'] = int(input('CTPS[0 não tem]: '))
if carteira['CTPS'] != 0:
    carteira['Ano de Contratação'] = int(input('Ano de Contratação: '))
    carteira['Salário'] = float(input('Salário:R$ '))
    carteira['Aposentadoria'] = (carteira['Ano de Contratação'] + 35) - ano_de_nascimento
print(carteira)
for k, v in carteira.items():
    print(f'{k} tem o valor {v}')
