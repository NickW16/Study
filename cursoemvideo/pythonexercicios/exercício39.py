from datetime import date
print('Este programa diz se um jovem já deveria ter se alistado nas forças armadas.')
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem 18 anos e deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você tem {} anos e já deveria ter se alistado há {} anos.'.format(idade, (idade-18)))
elif idade < 18:
    print('Você tem {} anos e deverá se alistar em {} anos.'.format(idade, (18-idade)))


