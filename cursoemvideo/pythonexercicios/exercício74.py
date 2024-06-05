###### este programa sorteia 5 números e os organiza #######
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))
for num in n:
    print('{}'.format(num), end=' ')
print(f'\nO maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')