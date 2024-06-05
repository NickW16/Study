from random import randint
from time import sleep
jogo = []
jogoslista = []
tot = 0
print('=-' * 30)
print('GERADOR DE JOGOS DA MEGA-SENA')
print('=-' * 30)
pergunta = int(input('Quantos jogos você quer jogar? '))
while tot <= pergunta:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogoslista.append(jogo[:])
    jogo.clear()
    tot += 1
print('Jogos sorteados: ')
for i, l in enumerate(jogoslista):
    print(f'Jogo {i+1}: {l}')
