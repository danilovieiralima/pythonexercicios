n = cont = media = maior = menor = s = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um número:'))
    r = str(input('Quer continuar?[S/N]')).upper()
    cont = cont + 1
    s = s + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = s / cont
print(f'Você digitou {cont} números. A soma deles é {s} e a média deles é {media:.2f}')
print(f'O maior número lido foi {maior} e o menor número lido foi {menor}')
print('FIM')
