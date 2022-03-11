jogador = dict()
jogador['Nome'] = str(input('Nome do Jogador: '))
total_de_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
gols_por_partida = list()
for c in range(0, total_de_partidas):
    gols_por_partida.append(int(input(f'   Quantos gols na partida {c+1}?')))
jogador['Gols por Partida'] = gols_por_partida[:]
jogador['Total de Gols'] = sum(gols_por_partida)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {total_de_partidas}')
for i, g in enumerate(gols_por_partida):
    print(f'   Na partida {i+1} fez {g} gols')
