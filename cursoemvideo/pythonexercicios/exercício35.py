print('Este programa diz se as 3 retas denominadas pelo usuário são capazes de formar um triângulo ou não.')
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 <r2+r1:
    print('Estas retas formam um triângulo!')
else:
    print('Estas retas não formam um triângulo...')