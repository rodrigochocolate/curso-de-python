from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
ranking = []
teste = []
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    ranking.append(v)
ranking.sort(reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
c = 1
for num in ranking:
    for k, v in jogadores.items():
        if num == v and teste.count(k) == 0:
            teste.append(k)
            print(f'   {c}º lugar: {k} com {v}.')
            sleep(1)
            c += 1