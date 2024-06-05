# Este programa pergunta números e depois os ordena de maneira crescente em uma lista #####
lista = []
while True:
    v = int(input('Digite um valor: '))
    if v in lista:
        print('O valor {} já está na lista. Valor não adicionado!'.format(v))
    else:
        lista.append(v)
    per = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if per in 'nN':
        break
lista.sort()
print('-='*30)
print('A lista digitada, em ordem crescente, foi: {}'.format(lista))
