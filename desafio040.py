n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2) / 2
if 7 > media >= 5:
    print(f'A média do aluno é {media} e ele está em RECUPERAÇÃO')
elif media < 5:
    print(f'A média do aluno é {media} e ele está REPROVADO')
elif media >= 7:
    print(f'A média do aluno é {media} e ele está APROVADO')
