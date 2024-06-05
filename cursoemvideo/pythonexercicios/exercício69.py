####### Este programa analisa dados e os organiza ######
print('-'*40)
print('CADASTRE UMA PESSOA: ')
homens = dezoito = mulvint = 0
while True:
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    cont = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens = homens + 1
    if idade > 18:
        dezoito = dezoito + 1
    if sexo == 'F' and idade < 20:
        mulvint = mulvint + 1
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        print('='*40)
        print('Foram contabilizadas:\n'
              'A) {} pessoas com mais de 18 anos\n'
              'B) {} homens cadastrados\n'
              'C) {} mulheres com menos de 20 anos.'.format(dezoito, homens, mulvint))
        print('Obrigado por utilizar este programa!')
        break
