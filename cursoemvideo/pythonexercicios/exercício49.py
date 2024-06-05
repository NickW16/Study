print('Este programa calcula uma tabuada.')
n = int(input('Digite um número: '))
soma = 0
tabu = 0
for c in range(0, 10):
    soma = n + soma
    tabu = tabu +1
    print('{} x {} = {}'.format(n, tabu, soma))
