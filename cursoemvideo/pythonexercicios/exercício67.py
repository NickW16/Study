#### Este programa calcula a tabuada de um número até 10 ####
n = 0
tab = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*20)
    if n <= 0:
        print('=' * 20)
        print('Número inválido. Programa encerrado.')
        break
    while tab != 10:
        tab += 1
        print('{} x {} = {}'.format(tab, n, (tab*n)))
    print('=' * 20)
print('Obrigado por utilizar este programa!')
