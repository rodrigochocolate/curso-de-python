lista = list()
par = list()
imp = list()
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {imp}')