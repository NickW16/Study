####### este programa organiza uma lista de números ######
lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont = cont + 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar not in 'Ss':
        break
print('=-'*30)
print(f'Você digitou {cont} elementos.')
print(f'A lista digitada foi: {lista}')
lista.sort(reverse=True)
print(f'A lista invertida é: {lista}')
if 5 in lista:
    print('O valor 5 está presente na lista!')
else:
    print('O valor 5 não foi encontrado!')


