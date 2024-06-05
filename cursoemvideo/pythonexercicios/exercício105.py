def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min (n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        else:
            r['situação'] = 'RUIM'
    return r


#
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)