def aumentar(preco = 0, taxa = 0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco = 0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>5.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('Resumo do Preço:'.center(30))
    print('-'*30)
    print(f'Preço analisado: {moeda(preco)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Aumentado em {taxaa}%: \t{aumentar(preco, taxaa, True)}')
    print(f'Diminuído em {taxar}%: \t{diminuir(preco, taxar, True)}')
    print('-'*30)