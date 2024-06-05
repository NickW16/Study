times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Atlético-PR', 'Internacional',
         'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('='*50)
print('Lista de times do Brasileirão 2023: {}'.format(times))
print('='*50)
print('Os 5 primeiros são: {}'.format(times[0:5]))
print('='*50)
print('Os 4 últimos são: {}'.format(times[-4:]))
print('='*50)
print('Os times em ordem alfabética são: {}'.format(sorted(times)))
print('='*50)
print('O Corinthians está na posição: {}'.format(times.index('Corinthians')+1))
