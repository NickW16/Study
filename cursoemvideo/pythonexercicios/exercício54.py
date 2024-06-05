import datetime
print('Este programa analisa a maioridade de pessoas de acordo com seu nascimento.')
maioridade = 0
menoridade = 0
cont = 0
hoje = datetime.date.today().year
for c in range(0, 7):
    cont = cont + 1
    idade = int(input('Digite a idade da pessoa n{}: '.format(cont)))
    if hoje - idade >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maioridade))
print('E, ao todo, tivemos {} pessoas menores de idade.'.format(menoridade))