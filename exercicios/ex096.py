'''def cab(txt):
    print(f'{txt:^22}')
    print('-' * 22)


def area(l, c):
    print(f'A área de um terreno {l}x{c} é de {l * c}m².')


cab('Controle de Terrenos')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))'''

# Solução do Curso em Vídeo
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)