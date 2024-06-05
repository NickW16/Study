print('Este programa soma 6 números. Mas somente os que forem pares.')
soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
    else:
        print('Valor ímpar. Número DESCONSIDERADO.')
        n = 0
print('A soma de {} números pares digitados é: {}'.format(cont,soma))