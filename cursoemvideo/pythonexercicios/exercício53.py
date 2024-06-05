print('Este programa identifica palíndromos.')
fr = str(input('Digite uma frase: ')).strip().upper()
palavras = fr.split()
junto = ''.join(palavras)
texto = junto [ : :-1]
"""Resolução do professor:
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!)
"""
print('{} escrito ao contrário é: {}.'.format(fr, texto))
if texto == junto:
    print('Esta frase é um palíndromo!')