from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já passou {idade - 18} anos da idade de alistamento')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para você ter idade suficiente para se alistar!')
