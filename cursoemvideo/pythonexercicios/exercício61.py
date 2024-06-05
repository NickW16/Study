########## este programa calcula uma PA #########
print('Gerador de PA: ')
print('='*40)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
while c != 11:
    print('{} > '.format(n),end='')
    n = n + r
    c = c + 1
print('FIM')
