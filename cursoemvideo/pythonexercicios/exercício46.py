import time
print('Este programa faz uma contagem regressiva.')
com = int(input('Digite "1" para começar: '))
if com == 1:
    for c in range(10, -1, -1):
        time.sleep(1)
        print(c)
    print('BOOOOOM!!!!!')
else:
    print('Número inválido.')