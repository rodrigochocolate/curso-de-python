def moeda(p):
    """
    -> Formata o preço
    :param p: coloca 'r$' no preço
    :return: retorna o preço formatado com ','
    """
    p = f'R${p:.2f}'
    return p.replace('.', ',')


def metade(p, formatar=False):
    """
    -> Calcula a metade de um preço
    :param p: recebe o preço
    :param formatar: (opcional) formatar ou não
    :return: retorna a metade do preço
    """
    p = p / 2
    if formatar:
        p = moeda(p)
    return p


def dobro(p, formatar=False):
    """
    -> Calcula o dobro de um preço
    :param p: recebe o preço
    :param formatar: (opcional) formatar ou não
    :return: retorna o dobro do preço
    """
    p = p * 2
    if formatar:
        p = moeda(p)
    return p


def aumentar(p, porc, formatar=False):
    """
    -> Aumenta o preço de acordo com a porcentagem lida
    :param p: recebe o preço
    :param porc: recebe a porcentagem
    :param formatar: (opcional) formatar ou não
    :return: retorna o preço aumentando
    """
    p = p + p * porc / 100
    if formatar:
        p = moeda(p)
    return p


def diminuir(p, porc, formatar=False):
    """
    -> Diminui o preço de acordo com a porcentagem lida
    :param p: recebe o preço
    :param porc: recebe a porcentagem
    :param formatar: (opcional) formatar ou não
    :return: retorna o preço diminuído
    """
    p = p - p * porc / 100
    if formatar:
        p = moeda(p)
    return p
