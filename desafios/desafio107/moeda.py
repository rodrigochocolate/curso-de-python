def metade(p):
    """
    -> Calcula a metade de um preço
    :param p: recebe o preço
    :return: retorna a metade do preço
    """
    return p / 2


def dobro(p):
    """
    -> Calcula o dobro de um preço
    :param p: recebe o preço
    :return: retorna o dobro do preço
    """
    return p * 2


def aumentar(p, porc):
    """
    -> Aumenta o preço de acordo com a porcentagem lida
    :param p: recebe o preço
    :param porc: recebe a porcentagem
    :return: retorna o preço aumentando
    """
    return p + p * porc / 100


def diminuir(p, porc):
    """
    -> Diminui o preço de acordo com a porcentagem lida
    :param p: recebe o preço
    :param porc: recebe a porcentagem
    :return: retorna o preço diminuído
    """
    return p - p * porc / 100
