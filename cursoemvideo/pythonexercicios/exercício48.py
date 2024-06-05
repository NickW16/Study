print('Este programa calcula a soma de todos os números ímpares, múltiplos de 3, entre 1 e 500.')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = c + soma
print('A soma de {} valores é {}.'.format(cont, soma))