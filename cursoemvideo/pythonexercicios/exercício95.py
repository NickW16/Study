#### aprimoramento do 93
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    part = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(0, part):
        partidas.append(int(input(f'Quantos gols {jogador['nome']} fez no jogo {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda com "S" ou "N"!')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('--------- VOLTE SEMPRE! ---------')