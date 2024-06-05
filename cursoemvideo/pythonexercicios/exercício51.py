print('Este programa calcula uma Progressão Aritmética.')
############## Introdução: #########
print('='*10, end=' ')
print('OS 10 TERMOS DE UMA PA: {}'.format('='*10))
############## Programa: ##########
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
res = 0
for c in range (0, 10):
    n = n + r
    print('{}'.format(n), end = ' - ')
print('FIM.')
