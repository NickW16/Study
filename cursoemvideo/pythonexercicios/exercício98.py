##### contador
from time import sleep
def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if c > 0:
        print(f'{a} ', end='')
        while a < b:
            a = a + c
            sleep(0.5)
            print(f'{a} ', end='')
    else:
        print(f'{a} ', end='')
        while a > b:
            a = a + c
            sleep(0.5)
            print(f'{a} ', end='')

contador(1, 10, 1)
print()
print('='*30)
contador(10, 0, -2)
print()
print('='*30)
######
print('Agora, realize a sua contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
