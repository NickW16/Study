import math
print('Este programa calcula o seno, cosseno e tangente de um determinado ângulo.')
ang = float(input('Digite um ângulo: '))
sen = float(math.sin(math.radians(ang)))
cos = float(math.cos(math.radians(ang)))
tan = float(math.tan(math.radians(ang)))
print('O seno de {} graus é: {:.2f}.'.format(ang, sen))
print('O cosseno de {} graus é: {:.2f}.'.format(ang, cos))
print('A tangente de {} graus é: {:.2f}.'.format(ang, tan))