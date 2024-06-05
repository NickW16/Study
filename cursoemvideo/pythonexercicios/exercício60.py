######## este programa calcula o fatorial de um número ########
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))