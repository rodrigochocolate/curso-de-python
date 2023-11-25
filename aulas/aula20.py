def lin(quanthif):
    print('-' * quanthif)


def cab(hifens, txt):
    print('-' * hifens)
    print(f'{txt:^{hifens}}')
    print('-' * hifens)


cab(30, 'CURSO EM VÍDEO')
cab(30, 'PYTHON É MUITO BOM')
cab(30, 'OI')