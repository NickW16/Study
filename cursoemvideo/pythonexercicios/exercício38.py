print('Este programa compara dois números e diz qual deles é o maior.')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1>n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n2>n1:
    print('{} é maior que {}.'.format(n2, n1))
else:
    print('Não existe valor maior. Os dois são iguais.')