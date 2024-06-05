######## Este programa organiza números digitados em 3 listas ####
lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar in 'Nn':
        break
print('-='*30)
print(f'A lista completa digitada foi: {lista}')
print(f'A lista com números pares foi: {listapar}')
print(f'A lista com números ímpares foi: {listaimpar}')
