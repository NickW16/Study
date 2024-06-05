#### programa de ctps ####
from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = (datetime.now().year - int(input('Ano de Nascimento: ')))
pessoa['ctps'] = int(input('CTPS: (Digite "0" para "não tem":) '))
if pessoa['ctps'] != 0:
    pessoa['anocontr'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = 35 - (datetime.now().year - pessoa['anocontr'])
print('----------- Resultado: -------------')
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v} ')

