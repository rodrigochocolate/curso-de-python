def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Aumenta o preço
    :param preço: (opcional) Preço que vai ser aumentado
    :param taxa: (opcional) Taxa de aumento
    :param formato: (opcional) Formatar ou não o preço
    :return: retorna o preço
    """
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Diminui o preço
    :param preço: (opcional) Preço que vai ser reduzido
    :param taxa: (opcional) Taxa de redução
    :param formato: (opcional) Formatar ou não o preço
    :return: retorna o preço
    """
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> Dobra o preço
    :param preço: (opcional) Preço que vai ser dobrado
    :param formato: (opcional) Formatar ou não o preço
    :return: retorna o preço
    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    -> Calcula a metade do preço
    :param preço: (opcional) Preço que vai ter sua metade calculada
    :param formato: (opcional) Formatar ou não o preço
    :return: retorna o preço
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    -> Formata o preço
    :param preço: (opcional) Preço que vai ser formatado
    :param moeda: (opcional) Moeda do preço
    :return: retorna preço formatado
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=0, taxar=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
