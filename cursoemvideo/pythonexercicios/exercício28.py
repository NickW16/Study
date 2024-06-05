import random
print('Este programa pensa em um número de 1 a 5 e verifica se o usuário o acertou.')
n = random.choice([1, 2, 3, 4, 5])
chute = str(input('O computador pensou em um número de 1-5. Tente acertar: '))
if chute == n:
    print('Parabéns, o número pensado foi {} e você acertou!'.format(n))
else:
    print('Você errou. O número pensado foi {}. Tente outra vez!'.format(n))