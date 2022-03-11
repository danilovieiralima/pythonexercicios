'''Dicionários --> {}'''
# FORMAS DE DECLARAR UM DICIONÁRIO
# dados = {}
# dados2 = dict()
# IDENTIFICANDO DADOS EM UM DICIONÁRIO
# dados3 = {'nome': 'Pedro', 'idade': 25}
# print(dados3['nome'])
# print(dados3['idade'])
# dados3['sexo'] = 'M'
# print(dados3)
# del dados3['idade']
# print(dados3)
'''filme0 = {'título': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'
          }
filme1 = {'título': 'Avengers',
          'ano': 2012,
          'diretor': 'Josh Whedon'}
filme2 = {'título': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachowski'}
# print(filme.values())
# print(filme.keys())
# print(filme.items())
# for k, v in filme.items():
#     print(f'O {k} é {v}')
locadora = []
locadora.append(filme0)
locadora.append(filme1)
locadora.append(filme2)
print(locadora)
print(locadora[0]['ano'])
print(locadora[1]['título'])
print(locadora[2]['título'])'''
'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)'''
brasil = list()
estado = dict()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
