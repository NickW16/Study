########## este programa calcula uma PA 2.0 #########
print('Gerador de PA: ')
print('='*40)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} > '.format(n),end='')
        n = n + r
        c = c + 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))