nome = str(input('Digite um nome: ')).strip()
separado = nome.split()
print('Seu primeiro nome é {}.'.format(separado[0]))
print('Seu último nome é {}.'.format(separado[len(separado)-1]))