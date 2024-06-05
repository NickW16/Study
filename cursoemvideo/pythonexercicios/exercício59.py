###### Este programa é uma calculadora com interface ######
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
running = 1
while running == 1:
    option = int(input('Escolha o que fazer:\n'
                       '[ 1 ] somar\n'
                       '[ 2 ] multiplicar\n'
                       '[ 3 ] maior\n'
                       '[ 4 ] novos números\n'
                       '[ 5 ] sair do programa\n'
                       '>>>>>>> Qual é a sua opção? '))
    if option == 1:
        print('=' * 30)
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    if option == 2:
        print('=' * 30)
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
    if option == 3:
        if n1 > n2:
            print('=' * 30)
            print('O maior número é {}.'.format(n1))
        if n2 > n1:
            print('=' * 30)
            print('O maior número é {}.'.format(n2))
        if n1 == n2:
            print('='*30)
            print('Os dois números são iguais.')
    if option == 4:
        print('=' * 30)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if option == 5:
        running = 0
    if option > 5:
        print('='*30)
        print('Opção inválida, tente novamente.')
print('Muito obrigado por utilizar esta calculadora!')
