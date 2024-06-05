## Este programa sorteia dados para 4 jogadores ##
from random import randint
import time
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou o número {v}')
    time.sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate (ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    time.sleep(1)