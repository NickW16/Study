######## este programa organiza pessoas por peso #######
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men == temp[1]
    else:
        if temp[1] > mai:
            temp[1] = mai
        if temp[1] < men:
            temp[1] = men
    princ.append(temp)
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg.', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print(f'O menor peso foi de {men}Kg.')