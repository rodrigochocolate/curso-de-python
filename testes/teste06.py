n = int(input('Digite um número para\ncalcular seu fatorial: '))
print(f'Calculando {n}! = ', end='')
c = n
r = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else f' = {r}', end='')
    r *= c
    c -= 1
