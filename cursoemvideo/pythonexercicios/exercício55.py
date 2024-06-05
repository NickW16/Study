print('Este programa avalia pesos e diz qual é o maior e o menor.')
cont = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG.'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))