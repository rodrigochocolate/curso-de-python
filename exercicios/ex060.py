n = int(input("""Digite um número para
calcular seu Fatorial: """))
print(f'Calculando {n}! = ', end='')
c = n
f = 1
while c != 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''