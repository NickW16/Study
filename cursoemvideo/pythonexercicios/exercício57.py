print('Este programa pergunta o sexo mas só aceita M ou F.')
n = 1
m = 'M'
f = 'F'
while n == 1:
    s = str(input('Digite o seu sexo (M/F): ')).upper()
    if s == m or s == f:
        n = 0
        print('Você digitou {}, obrigado!.'.format(s))
    else:
        n = 1
        print('Sexo inválido.')
""" 
sexo = str(input('Digite o seu sexo (M/F): ').strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Sexo inválido. Digite novamente (M/F): ').strip().upper()[0]
print('Sexo {} registrado com sucesso.')"""