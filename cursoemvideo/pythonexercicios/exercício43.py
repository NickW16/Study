print('Este programa calcula o IMC de uma pessoa.')
p = float(input('Digite o seu peso (KG): '))
a = float(input('Digite a sua altura (cm): '))
am = a/100
imc = p/(am**2)
if imc<=18.5:
    print('IMC = {:.1f}. Você está abaixo do peso.'.format(imc))
elif imc>=18.5 and imc<=25:
    print('IMC = {:.1f}. Peso ideal.'.format(imc))
elif imc>25 and imc<=30:
    print('IMC = {:.1f}. Sobrepeso.'.format(imc))
elif imc>30 and imc<=40:
    print('IMC = {:.1f}. Obeeeeeso.'.format(imc))
else:
    print('Obesidade mórbida.')