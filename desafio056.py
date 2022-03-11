somaidade = 0
nomehomemvelho = ''
homemmaioridade = 0
totmulher20 = 0
mediaidade = 0
for p in range(1, 5):
    print(f'{p} PESSOA')
    nome = str(input(f'Digite o nome da {p} pessoa:')).strip()
    idade = int(input(f'Digite a idade da {p} pessoa:'))
    sexo = str(input(f'Digite o sexo da {p} pessoa [M/F]:'))
    somaidade = somaidade + idade
    if sexo in 'Mm' and idade > homemmaioridade:
        homemmaioridade = idade
        nomehomemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho se chama {nomehomemvelho} e tem {homemmaioridade} anos de idade')
print((f'Ao todo são {totmulher20} mulheres com menos de 20 anos'))
