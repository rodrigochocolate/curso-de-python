info = dict()
info['nome'] = str(input('Nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {info["nome"]} jogou? '))
info['gols'] = []
info['total'] = 0
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    info['gols'].append(gol)
    info['total'] += info['gols'][c]
print('-=' * 30)
print(info)
print('-=' * 30)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {info["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {info["gols"][c]} gols.')
print(f'Foi um total de {info["total"]} gols.')