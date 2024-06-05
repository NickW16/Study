##### sorteia e soma, funções #####
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista...')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} -', end=' ')
        sleep(0.3)
def somapar(lista):
    total = 0
    for valor in lista:
        if valor % 2 == 0:
            total += valor
    print(f'A soma dos números pares desta lista é {total}.')

numeros = []
sorteia(numeros)
somapar(numeros)
