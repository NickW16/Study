print('Este programa calcula o valor de um produto.')
print('{:=^40}'.format(' LOJAS GUANABARA '))
p = float(input('Digite o preço do produto: R$'))
cond = int(input('Digite a condição desejada de pagamento:\n'
                 'Digite 1 para À VISTA NO DINHEIRO(10%desc)\n'
                 'Digite 2 para À VISTA NO CARTÃO(5%desc)\n'
                 'Digite 3 para EM ATÉ 2X, NO CARTÃO(preço normal)\n'
                 'Digite 4 para 3X OU MAIS, NO CARTÃO(20%juros): '))
if cond == 1:
    v = (p*0.9)
    print('O preço do produto com 10% de desconto será R${:.2f}.'.format(v))
elif cond == 2:
    v = (p*0.95)
    print('O preço do produto com 5% de desconto será R${:.2f}.'.format(v))
elif cond == 3:
    v = p
    print('O preço do produto ficará R${:.2f}.'.format(v))
elif cond == 4:
    v = (p*1.2)
    print('O preço com 20% de juros será R${:.2f},'.format(v))
else:
    p = 0
    print('Leia de novo.')
