print('Este programa pergunta um monte de coisas e organiza.')
cont = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulheres = 0
for dados in range(1, 5):
    cont = cont + 1
    print('='*10,' {}a pessoa: '.format(cont), '='*10)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): '))
    somaidade = somaidade + idade
    if dados == 1 and sexo in ('Mm'):
        maioridadehomem = idade
        nomevelho = nome
    if sexo in ('Mm') and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in ('Ff') and idade < 20:
        totmulheres = totmulheres + 1
print('A média das idades é {}.'.format(somaidade/cont))
print('O homem mais velho é o {} e sua idade é {}.'.format(nomevelho, maioridadehomem))
print('Neste grupo, há {} mulheres com menos de 20 anos.'.format(totmulheres))