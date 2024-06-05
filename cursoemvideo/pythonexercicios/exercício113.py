def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            break
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número válido.')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            break
        else:
            return n


###
n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'O número inteiro foi {n1} e o real foi {n2}.')