import math
print('Este programa calcula a hipotenusa de um triângulo retângulo.')
lado1 = float(input('Digite o cateto oposto: '))
lado2 = float(input('Digite o cateto adjacente: '))
hipo = math.hypot(lado1, lado2)
print('A hipotenusa do triângulo é: {}'.format(hipo))