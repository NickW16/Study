list = []
v = 0
while v < 5:
    list.append(int(input('Digite um valor para a posição {}: '.format(v))))
    v = v + 1
listordenada = sorted(list)
menor = min(list)
posicoesmenor = [i for i, v in enumerate(list) if v == menor]
maior = max(list)
posicoesmaior = [i for i, v in enumerate(list) if v == maior]
print('Você digitou os valores {}'.format(list))
print('O menor valor foi {}, nas posições {}.'.format(menor, posicoesmenor))
print('O maior valor foi {} nas posições {}.'.format(maior, posicoesmaior))