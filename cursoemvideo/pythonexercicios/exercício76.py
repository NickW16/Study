########## este programa organiza preços #######
prec = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
        'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso',
        9.99, 'Mochila', 120.32, 'Canetas', 22.30,
        'Livro', 34.90)
print('-'*30)
print('LISTAGEM DE PREÇOS:')
print('-'*30)
for n in range(0, len(prec)):
    if n % 2 == 0:
        print(f'{prec[n]:.<30}', end=' ')
    else:
        print(f'R${prec[n]}')