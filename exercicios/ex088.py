'''from time import sleep
from random import randint
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
lista = []
for c in range(1, n + 1):
    lista.append([randint(1, 60), randint(1, 60), randint(1, 60),
                  randint(1, 60), randint(1, 60), randint(1, 60)])
    for lis in lista:
        for num in lis:
            while lis.count(num) > 1:
                lis.remove(num)
                lis.append(randint(1, 60))
    print(f'Jogo {c}: {sorted(lista[c - 1])}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')'''

# Solução do Curso em Vídeo
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, F'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
