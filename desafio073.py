t = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corithians', 'Fortaleza',
     'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Ceará-SC',
     'Santos', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiába',
     'Bahia', 'Juventude', 'Grêmio', 'Sport Recife', 'Chapecoense')
print('=' * 60)
print(f'A Lista de Times é:{t}')
print('=' * 60)
print(f'Os cinco primeiros times colocados são: '
      f'{t[0:5]}')
print('=' * 60)
print(f'Os últimos 4 colocados são:{t[16:]}')
print('=' * 60)
print(f'''A lista dos times em ordem alfabética é 
{sorted(t)}''')
print('=' * 60)
print(f'O time da Chapecoense está na posição {t.index("Chapecoense") + 1}')
print('=' * 60)
