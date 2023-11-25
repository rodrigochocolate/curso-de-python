'''from time import sleep

def lin():
    print('-=' * 30)


def contador(i, f, p):
    if p == 0:
        p = 1
    p = str(p)
    print(f'Contagem de {i} até {f} de {p[1:] if p[0] == "-" else p} em {p[1:] if p[0] == "-" else p}')
    p = int(p)

    if i > f and p > 0:
        p = -p
    if p < 0:
        f -= 1

    else:
        f += 1
    sleep(1)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.25)
    print('FIM!')


lin()
contador(1, 10, 1)
lin()
contador(10, 0, -2)
lin()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
lin()
contador(i, f, p)'''

# Solução Curso em Vídeo
from time import sleep


def contador(i, f, p):
    sleep(1)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont -= p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)