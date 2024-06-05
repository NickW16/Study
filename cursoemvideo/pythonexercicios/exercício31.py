print('Este programa calcula o preço por km/hr de uma viagem de ônibus.')
dist = int(input('Qual foi a distância da viagem (em km/hr)? '))
if dist > 200:
    print('Viagem com desconto! O preço é: R${}.'.format(dist*0.45))
else:
    print('Viagem SEM desconto! O preço é: R${}.'.format(dist*0.50))