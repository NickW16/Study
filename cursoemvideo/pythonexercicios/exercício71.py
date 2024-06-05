######### este programa calcula as cédulas de saque de um caixa eletrônico ########
print('='*40)
print('BANCO NICK')
print('='*40)
notas50 = notas20 = notas10 = notas1 = 0
v = int(input('Qual valor você deseja sacar? R$'))
total = v
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print('Total de {} cédulas de R${}'.format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 1:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Operação finalizada.')