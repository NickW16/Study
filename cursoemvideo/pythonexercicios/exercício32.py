import datetime
print('Este programa verifica se o ano digitado é bissexto ou não.')
ano = int(input('Digite um ano (Digite 0 para avaliar o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano não é bissexto.')