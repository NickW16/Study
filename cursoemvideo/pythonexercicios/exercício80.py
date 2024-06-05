##### Este programa pergunta números e os ordena ####
lista = []
cont = 0
while True:
    cont = cont + 1
    n = int(input('Digite um valor: '))
    if cont == 1 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista(pos):
                lista.insert(pos, n)
                break
            pos = pos + 1
print('-=' * 30)
print('Os valores digitados, em ordem, foram {}'.format(lista))
