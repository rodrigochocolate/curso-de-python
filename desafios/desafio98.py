from time import sleep


def linha():
    print('-=' * 20)


def contagem(i, f, p):
    print(f'Contagem de {i} até {f} de ', end='')
    if p == 0:
        p = 1
    if i > f and p > 0:
        p = -p # Ou p - (p * 2)
    if p < 0:
        p = str(p)
        print(f'{p[1:]} em {p[1:]}')
        p = int(p)
        f -= 1
    else:
        print(f'{p} em {p}')
        f += 1
    sleep(1)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.25)
    print('FIM!')


linha()
contagem(1, 10, 1)
linha()
contagem(10, 0, -2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
linha()
contagem(i, f, p)
