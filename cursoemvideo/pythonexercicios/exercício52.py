print('Este programa verifica se um número é primo ou não.')
n = int(input('Digite um número: '))
cont = 0
vezes = 0
for c in range(1, n + 1 ):
    vezes = vezes + 1
    if n % vezes == 0:
        print('\033[34m'.format(n), end=' ')
        cont = cont + 1
    else:
        print('\033[32m'.format(n), end=' ')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, cont))
if cont == 2:
    print('O número digitado É PRIMO!')
else:
    print('O número digitado NÃO É PRIMO!')