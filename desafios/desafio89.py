lista = []
while True:
    lista.append([str(input('Nome: ')).title(), [float(input('Nota 1: ')), float(input('Nota 2: '))]])
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'No. NOME{"MÉDIA":>16}')
print('-' * 48)
for c in range(0, len(lista)):
    print(f'{c:<4}{lista[c][0]:>4}{(lista[c][1][0] + lista[c][1][1]) / 2:>{len(lista[c][0]) - 20}.1f}')
print('-' * 48)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        break
    else:
        print(f'Notas de {lista[notas][0]} são {lista[notas][1]}')
        print('-' * 48)
print('<<< VOLTE SEMPRE >>>')