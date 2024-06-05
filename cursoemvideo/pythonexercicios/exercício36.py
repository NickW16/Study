print('Este programa diz se é possível realizar um financiamento de um imóvel.')
v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o salário do comprador: R$'))
a = int(input('Digite em quantos anos pretende pagar o imóvel: '))
p = float(v/(a*12))
if (p>=(s*0.3)):
    print('A parcela seria de R${:.2f}.'.format(p))
    print('Seu salário não é suficiente para o financiamento. Empréstimo negado.')
else:
    print('Você atende às condições do empréstimo. Parabéns!')
    print('A parcela será de R${:.2f}'.format(p))