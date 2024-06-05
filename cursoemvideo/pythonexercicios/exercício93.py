###### programa de cálculo de gols #####
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, part):
    partidas.append(int(input(f'Quantos gols {jogador['nome']} fez no jogo {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=#'*30)
print(jogador)
print('=#'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=#'*30)
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador['total']} gols')
