'''lista = []
while True:
    lista.append([str(input('Nome: ')).title(), [float(input('Nota 1: ')), float(input('Nota 2: '))]])
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print('No. NOME         MÉDIA')
print('-' * 26)
for c in range(0, len(lista)):
    media = (lista[c][1][0] + lista[c][1][1]) / 2
    print(f'{c:<4}{lista[c][0]:<14}{media:4.1f}')
print('-' * 35)
while True:
    notas = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {lista[notas][0]} são {lista[notas][1]}')
    print('-' * 35)'''

# Solução do Curso em Vídeo
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')
