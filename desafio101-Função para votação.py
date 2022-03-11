def voto(anodenascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - anodenascimento
    if idade < 16:
        return f'Com {idade} anos:Voto NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos:Voto OPCIONAL'
    else:
        return f'Com {idade} anos:Voto OBRIGATÓRIO'


print(voto(2000))
print(voto(2003))
print(voto(1950))
print(voto(1980))
print(voto(2004))
print(voto(2010))
