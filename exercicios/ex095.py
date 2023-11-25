'''jogadores = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] '))[0].upper()
        if resp in 'SN':
            break
        print('ERRO! Você deve digitar S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod"}{"nome":>5}{"gols":>15}{"total":>16}')
print('-' * 40)
for pos, j in enumerate(jogadores):
    print(f'{pos:>3} {j["nome"]:<15}{str(j["gols"]):<15}{j["total"]}')
while True:
    print('-' * 40)
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while 999 != dados >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {dados}!')
        dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}:')
    for c in range(0, len(jogadores[dados]["gols"])):
        print(f'    No jogo {c + 1} fez {jogadores[dados]["gols"][c]}')
print('<< VOLTE SEMPRE >>')'''

# Solução do Curso em Vídeo
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
