from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for c in range(1, n + 1):
    print(f'Jogo {c}: ', end='')
    lista = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    for cont in range(0, 6):
        while lista.count(lista[cont]) > 1:
            lista[cont] = randint(1, 60)
    print(sorted(lista))
    sleep(0.5)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
