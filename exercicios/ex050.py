soma_pares = 0
pares = 0
for c in range(1, 7):
    n = int(input(f'{c}º valor: '))
    if n % 2 == 0:
        soma_pares += n
        pares += 1
print(f'Dos 6 valores digitados {pares} são pares e a soma entre eles é {soma_pares}')