n1 = int(input('Digite um número inteiro: '))
print(f'O dobro de {n1} é {n1 * 2}')
print(f'O triplo de {n1} é {n1 * 3}')
r1 = n1 ** 0.5
r2 = str(f'{r1:.2f}')
if '.00' in r2:
    r2 = f'{n1 ** 0.5:.0f}'
print(f'A raiz quadrada de {n1} é {r2}')
