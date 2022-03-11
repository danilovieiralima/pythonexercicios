from datetime import date
maior18 = 0
menor18 = 0
igual18 = 0
for p in range(1, 8):
    print(f'{p} PESSOA')
    nasc = int(input(f'Ano de Nascimento da {p} pessoa:'))
    atual = date.today().year
    idade = atual - nasc
    print(f'A {p} pessoa nasceu em {nasc} e tem {idade} anos de idade')
    if idade > 18:
        maior18 = maior18 + 1
    if idade < 18:
        menor18 = menor18 + 1
    if idade == 18:
        igual18 = igual18 + 1
print(f'A quantidade de pessoas maiores de 18 anos é {maior18}')
print(f'A quantidade de pessoas menores de 18 anos é {menor18}')
print(f'A quantidade de pessoas com 18 anos é {igual18}')
