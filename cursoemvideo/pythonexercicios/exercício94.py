######## calculadora e organizadora de nomes e idades
pessoa = {}
grupo = []
soma = média = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if pessoa['sexo'] not in 'MmFf':
        print('Sexo inválido.\n'
        'Programa encerrado. Tente novamente.')
        break
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    grupo.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar not in 'Ss':
        break
print(f'A) Ao todo, temos {len(grupo)} pessoas cadastradas')
print(f'B) A soma das idades é {soma}')
média = soma / len(grupo)
print(f'C) A média das idades é {média:5.2f}')
print(f'D) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print('E) Lista das pessoas que estão acima da média de idade: ')
for p in grupo:
    if p['idade'] > média:
        print(f'{p['nome']}', end='')
