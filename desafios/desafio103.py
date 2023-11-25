def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nomeJog = str(input('Nome do jogador: ')).strip()
totGols = str(input('Número de Gols: ')).strip()
if totGols == '' == nomeJog:
    ficha()
else:
    if totGols == '' != nomeJog:
        ficha(nome=nomeJog)
    elif totGols != '' == nomeJog:
        ficha(gols=totGols)
    else:
        ficha(nome=nomeJog, gols=totGols)