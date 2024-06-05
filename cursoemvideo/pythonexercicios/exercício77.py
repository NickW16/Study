########## este programa verifica vogais em palavras ########
pala = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
        'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
        'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in pala:
    print('\nNa palavra {} temos '.format(p), end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')