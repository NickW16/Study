######## este programa serve de relatório de loja ######
print('-'*40)
print('Lojas nick')
total = milmais = menor = cont = 0
barato = ''
while True:
    print('-' * 40)
    prod = str(input('Nome do produto: '))
    prec = float(input('Preço: R$'))
    cont = cont + 1
    continuar = ' '
    total = total + prec
    if prec > 1000:
        milmais = milmais + 1
    if cont == 1:
        menor = prec
        barato = prod
    else:
        if prec < menor:
            menor = prec
            barato = prod
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*40)
print('O gasto total da compra foi R${:.2f}.'.format(total))
print('{} produtos custaram mais que R$1000.00.'.format(milmais))
print('O produto mais barato é o(a) {} e custa R${:.2f}.'.format(barato, menor))