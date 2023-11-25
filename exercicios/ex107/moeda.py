'''def metade(p):
    metade = p / 2
    return metade


def dobro(p):
    dobro = p * 2
    return dobro


def aumento(p, porc):
    aumento = p + (p * porc / 100)
    return aumento'''

def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
