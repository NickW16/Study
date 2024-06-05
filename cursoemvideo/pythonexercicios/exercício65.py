########### este programa lê vários números, calcula a média e diz quais foram o maior e o menor número ##########
r = 'sS'
cont = soma = maior = menor = 0
while r not in ('Nn'):
    n = int(input('Digite um número: '))
    soma = soma + n
    cont = cont + 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = (soma/cont)
print('Você digitou {} números e a média foi {}. '.format(cont, media))
print('O maior valor foi {} e o menor foi {}. '.format(maior, menor))

