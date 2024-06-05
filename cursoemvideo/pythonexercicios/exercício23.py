print('Este programa lê um número de 0 a 9999 e o classifica.')
num = int(input('Digite um valor: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000% 10
print('Unidades = {}'.format(unidade))
print('Dezenas = {}'.format(dezena))
print('Centenas = {}'.format(centena))
print('Milhares = {}'.format(milhar))
