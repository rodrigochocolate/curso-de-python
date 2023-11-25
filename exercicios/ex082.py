lista = []
par = []
imp = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'a lista de ímpares é {imp}')