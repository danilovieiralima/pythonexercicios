time = list()
jogador = dict()
gols_por_partida = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    total_de_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols_por_partida.clear()
    for c in range(0, total_de_partidas):
        gols_por_partida.append(int(input(f'   Quantos gols na partida {c+1}?')))
    jogador['Gols'] = gols_por_partida[:]
    jogador['Total'] = sum(gols_por_partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Erro!Digite apenas S ou N!')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<11}{"gols":<15} Total')
for k, v in enumerate(time):
    print(f'{k:<4}{v["Nome"]:<11}{str(v["Gols"]):<18}{v["Total"]}')
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('ENCERRADO')
