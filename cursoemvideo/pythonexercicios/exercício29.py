print('Este programa lê a velocidade do carro e diz se ele foi multado ou não.')
vel = int(input('Digite a velocidade do veículo (km/hr): '))
if vel>80:
    print('Limite excedido! Você será multado em R${:.2f}.'.format((vel-80)*7))
else:
    print('Velocidade normal.')