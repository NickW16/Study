print('Este programa calcula aumento de salários.')
nome = str(input('Digite o nome do funcionário: '))
sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250.00:
    print('O novo salário de {} com aumento de 10% será R${:.2f}.'.format(nome,(sal*1.10)))
else:
    print('O novo salário de {} com aumento de 15% será R${:.2f}.'.format(nome,(sal*1.15)))



