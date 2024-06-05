###### este exercício calcula uma fatorial
def fatorial(n, show=False):
    """
    Esta função calcula uma fatorial.
    :param n: Número base
    :param show: mostrar ou não os processos
    :return: resultado do cálculo fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f

# Programa principal
print(fatorial(5, show=True))