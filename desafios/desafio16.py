from math import trunc
try:
    n1 = float(input('Digite um número qualquer: '))
    print(f'\nA parte inteira de {n1} é {trunc(n1)}')
except ValueError:
    print('\033[31mERRO!')
finally:
    print()