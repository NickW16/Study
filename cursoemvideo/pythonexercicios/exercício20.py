import random
print('Este programa sorteia uma ordem entre determinados objetos.')
alu1 = str(input('Digite o nome do primeiro aluno: '))
alu2 = str(input('Digite o nome do segundo aluno: '))
alu3 = str(input('Digite o nome do terceiro aluno: '))
alu4 = str(input('Digite o nome do quarto aluno: '))
res = [alu1, alu2, alu3, alu4]
random.shuffle(res)
print('A ordem foi {}.'.format(res))

