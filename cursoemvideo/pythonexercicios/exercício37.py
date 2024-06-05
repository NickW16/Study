print('Este programa lê um número inteiro e o converte.')
n = int(input('Digite um número: '))
escolha = int(input('Escolha uma base:\n'
                    '1 para binário\n'
                    '2 para octal\n'
                    '3 para hexadecimal: '))
if escolha == 1:
    print('O número {} em base binária é {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print(' O número {} em base octal é {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} em base hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('O número digitado não atende ao suportado por este programa.')
