a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print(f'O maior número dos três valores é {maior}')
# SEGUNDO JEITO DE FAZER:
lista = []
for n in range(1, 4):
    n1 = float(input(f'{n}º número: '))
    lista.append(n1)
print(f'O maior número dos três valores é {max(lista)}')