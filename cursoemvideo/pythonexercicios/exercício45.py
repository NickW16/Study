import random
import time
print('Este programa é um jogo de Joukenpo')
sel = str(input('Dentre estes, selecione uma opção:\n'
                'A: Pedra\n'
                'B: Papel\n'
                'C: Tesoura\n'
                'Opção: '))
if sel == ('a'):
    sel = 'Pedra'
elif sel == ('b'):
    sel = 'Papel'
elif sel == ('c'):
    sel = 'Tesoura'
else:
    sel = 'nenhuma das opções'
    print('Digite novamente.')
################  resultado player: #########
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('Você escolheu {}!'.format(sel))

################ cálculo bot: #############
bota = ('Pedra')
botb = ('Papel')
botc = ('Tesoura')
botoption = random.choice([bota, botb, botc])
print('O computador escolheu {}!'.format(botoption))

############### resultados: ##########
if sel == ('Pedra') and botoption == ('Tesoura'):
    print('Você venceu!')
elif sel == ('Papel') and botoption == ('Pedra'):
    print('Você venceu!')
elif sel == ('Tesoura') and botoption == ('Papel'):
    print('Você venceu!')
elif sel == botoption:
    print('Deu empate!')
else:
    print('Você perdeu. A máquina venceu!')




