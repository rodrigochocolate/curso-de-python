'''from random import randint
from time import sleep
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ordem = []
print('Valores sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    ordem.append(v)
ordem.sort(reverse=True)
ranking = {}
for n in ordem:
    for k, v in dados.items():
        if n == v:
            ranking[k] = n
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
pos = 1
for k, v in ranking.items():
    print(f'   {pos}º lugar: {k} com {v}')
    sleep(1)
    pos += 1'''

# Solução do Curso em Vídeo
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)