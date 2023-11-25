def somar(a=0, b=0, c=0):
    """
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Rodrigo bento
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar()
somar(2, 4)
somar(b=4, c=2)
somar(c=2, b=4)
