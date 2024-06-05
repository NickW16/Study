print('Este programa qual tipo de triângulo é possível formar.')
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 <l2+l1:
    print('Estas retas formam um triângulo!')
    if l1 == l2 == l3:
        print('Estes lados formam um triângulo Equilátero.')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Estes lados formam um triângulo Isósceles.')
    else:
        print('Estes lados formam um triângulo Escaleno.')
else:
    print('Estas retas não formam um triângulo...')
