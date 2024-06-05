############ este programa soma todos os números digitados ###########
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        n = 0
        break
    soma = soma + n
    cont = cont + 1
print('A soma de {} números digitados foi {}.'.format(cont, soma))