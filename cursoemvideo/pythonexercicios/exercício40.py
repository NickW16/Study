print('Este programa diz a situação de um aluno de acordo com suas notas.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1+n2)/2)
if m<5.0:
    print('Sua média foi {:.1f}. Você foi REPROVADO.'.format(m))
elif m>5.0 and m<7.0:
    print('Sua média foi {:.1f}. Você está de RECUPERAÇÃO.'.format(m))
else:
    print('Sua média foi {:.1f}. Você foi APROVADO. Parabéns!'.format(m))