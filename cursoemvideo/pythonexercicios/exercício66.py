######## Este programa soma números que não sejam 999 ########
n = 0
cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para finalizar): '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print('='*30)
print('Foram digitados {} números.\n'
      'A soma deles é {}.'.format(cont, soma))