from random import randint

lista = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
    print('PRONTO!')


def somaPar():
    soma_par = 0
    for v in lista:
        if v % 2 == 0:
            soma_par += v
    print(f'Somando os valores pares de {lista}, temos {soma_par}')


sorteia()
somaPar()