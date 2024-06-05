c = ('\033[m', ## sem cor
     '\033[0:30:41m' ## vermelho
     ''
 )

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

## Programa principal:
comando = ''
while True:
    título('Sistema de ajuda PYHELP', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!', 1)