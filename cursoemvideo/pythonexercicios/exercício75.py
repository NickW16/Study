######## este programa analisa dados ########
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro valor 3 apareceu na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares foram:', end =' ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')