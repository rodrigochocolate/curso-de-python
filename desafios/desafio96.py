def cab(txt):
    print(txt)
    print('-' * len(txt))


def area(lar, com):
    print(f'A área de um terreno {lar}x{com} é de {lar * com}m².')


cab('Controle de Terrenos')
area(lar=float(input('LARGURA (m): ')), com=float(input('COMPRIMENTO (m): ')))