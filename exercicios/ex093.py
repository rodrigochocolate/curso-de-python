'''info = dict()
info['nome'] = str(input('Nome do Jogador: ')).title()
partidas = int(input('Quantas partidas Zico jogou? '))
info['gols'] = list()
info['total'] = 0
for c in range(0, partidas):
    info['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    info['total'] += info['gols'][c]
print('-=' * 30)
print(info)
print('-=' * 30)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {info["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {info["gols"][c]} gols.')
print(f'Foi um total de {info["total"]} gols.')'''

# Solução do Curso em Vídeo
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')