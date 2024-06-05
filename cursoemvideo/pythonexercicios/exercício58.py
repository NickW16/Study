import random
#### Este programa pensa em um número de 0 a 10 e o jogador tem que adivinhar.
print('Eu sou seu computador...')
print('Pensei em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
nc = random.randint(0,10)
chute = int(input('Qual o seu chute? '))
if chute < nc:
    print('Mais...')
if chute > nc:
    print('Menos...')
palpites = 1
while chute != nc:
    chute = int(input('Você errou!\nTente novamente: '))
    palpites = palpites + 1
    if chute < nc:
        print('Mais...')
    if chute > nc:
        print('Menos...')
print('Você acertou com {} tentativas! Eu pensei {} e você também!'.format(palpites, nc))