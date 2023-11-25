lista = list()
while True:
    info = dict()
    info['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas {info["nome"]} jogou? '))
    info['gols'] = []
    info['total'] = 0
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c}? '))
        info['gols'].append(gol)
        info['total'] += gol
    lista.append(info.copy())
    resp = str(input('Quer continuar? [S/N] '))[0].upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))[0].upper()
    print('-' * 30)
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"cod"}{"nome":>5}{"gols":>15}{"total":>15}')
print('-' * 39)
for c, j in enumerate(lista):
    a = len(str(j["gols"])) - 15
    print(f'{c:>3} {j["nome"]:<15}{j["gols"]}{j["total"]:>{a}}')
print('-' * 39)
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    elif dados >= len(lista):
        print(f'ERRO! Não existe jogador com o código {dados}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[dados]["nome"]}:')
        for c, g in enumerate(lista[dados]["gols"]):
            print(f'   No jogo {c} fez {g} gols.')
    print('-' * 39)
print('<< VOLTE SEMPRE >>')