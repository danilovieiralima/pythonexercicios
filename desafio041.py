from datetime import date

nasc = int(input('Ano de nascimento do Atleta:'))
atual = date.today().year
idade = atual - nasc
print(f'O atleta nasceu em {nasc} e tem {idade} anos')
print('Qual a categoria desse atleta?')
if idade <= 9:
    print('A categoria do Atleta é MIRIM')
elif idade <= 14:
    print('A categoria do Atleta é INFANTIL')
elif idade <= 19:
    print('A categoria do Atleta é JUNIOR')
elif idade <= 25:
    print('A categoria do atleta é SENIOR')
elif idade > 25:
    print('A categoria do atleta é MASTER')
