from random import choice
print('Este programa escolhe aleatoriamente entre determinadas opções.')
alu1 = str(input('Digite o nome do primeiro aluno: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
options = [alu1, alu2, alu3, alu4]
res = random.choice(options)
print('O escolhido foi: {}'.format(res))