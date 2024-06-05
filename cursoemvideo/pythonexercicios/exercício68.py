########## Este programa é um jogo de par ou ímpar ######
import random
n = contv = npc = 0
resultado = ''
print('Jogo de par ou ímpar!')
while True:
    print('-' * 40)
    n = int(input('Escolha um número (até 10): '))
    npc = random.randrange(0,11)
    opc = str(input('Par ou ímpar? (P/I): ')).strip().upper()[0]
    print('='*40)
    print('O computador escolheu {} e você escolheu {}!'.format(npc, n))
    print('Deu PAR!'if (n+npc)%2==0 else 'Deu ÍMPAR!')
    if opc not in 'PI':
        print('Resposta inválida.')
        opc = ''
    if n > 10:
        print('Número inválido. Jogo encerrado.')
        break
    if (n + npc) % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if opc == resultado:
        print('='*40)
        print('Parabéns, você venceu! Jogue novamente!')
        contv = contv + 1
    else:
        print('='*40)
        print('Você perdeu! Até aqui, você derrotou o CPU {} vezes!'.format(contv))
        break

