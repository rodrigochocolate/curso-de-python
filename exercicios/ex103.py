'''def ficha(nome='<desconhecido>', gols=0):
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nomeJog = str(input('Nome do Jogador: ')).strip()
totgols = str(input('Número de Gols: ')).strip()
if totgols != '':
    int(totgols)
if totgols != '' != nomeJog:
    ficha(nomeJog, totgols)
elif totgols == '' == nomeJog:
    ficha()
elif totgols != '' == nomeJog:
    ficha(gols=totgols)
else:
    ficha(nomeJog)'''

# Solução do Curso em Vídeo


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)