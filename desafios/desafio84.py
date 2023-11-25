galera = []
dado = []
pesos = []
while True:
    dado.append(str(input('Nome: ')))
    peso = (float(input('Peso: ')))
    dado.append(peso)
    pesos.append(peso)
    galera.append(dado[:])
    dado.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('-=' * 40)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {max(pesos)}Kg. Peso de ', end='')
for p in galera:
    if p[1] == max(pesos):
        print(f'[{p[0].title()}]', end=' ')
print(f'\nO menor peso foi de {min(pesos)}Kg. Peso de ', end='')
for p in galera:
    if p[1] == min(pesos):
        print(f'[{p[0].title()}]', end=' ')
print()
