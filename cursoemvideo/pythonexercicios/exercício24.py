print('Este programa diz se há "SANTO" no nome de uma cidade ou não.')
nome = str(input('Digite o nome de uma cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')
