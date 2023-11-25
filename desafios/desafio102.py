def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
    return f


print('-' * 30)
print(fatorial(3, show=True))
help(fatorial)