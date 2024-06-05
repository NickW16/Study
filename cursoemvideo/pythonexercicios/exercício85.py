## este programa organiza números pares e ímpares ##
lista = []
numpar = []
numimpar = []
cont = 0
for c in range(0, 7):
    cont += 1
    n = int(input(f'Digite o {cont}o valor: '))
    lista.append(n)
    if n % 2 == 0:
        numpar.append(n)
    else:
        numimpar.append(n)
lista.sort()
numpar.sort()
numimpar.sort()
print('=-=' * 14)
print('           RESULTADO: ')
print('=-=' * 14)
print(f'A lista completa é {lista}')
print(f'Os números pares são {numpar}')
print(f'Os números ímpares são {numimpar}')