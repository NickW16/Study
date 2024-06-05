from datetime import date
print('Este programa diz a categoria de um competidor de acordo com a sua idade.')
a = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual-a
if idade<=9:
    print('Você tem {} anos e é da categoria MIRIM.'.format(idade))
elif idade<=14:
    print('Você tem {} anos e é da categoria INFANTIL.'.format(idade))
elif idade<=19:
    print('Você tem {} anos e é da categoria JÚNIOR.'.format(idade))
elif idade<=25:
    print('Você tem {} anos e é da categoria SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos e é da categoria MASTER.'.format(idade))

