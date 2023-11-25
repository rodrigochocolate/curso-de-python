matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
for linha in range(0, 3):
    for pos in range(0, 3):
        matriz[linha][pos] = int(input(f'Digite um valor para [{linha}, {pos}]: '))
        if matriz[linha][pos] % 2 == 0:
            soma_pares += matriz[linha][pos]
        if pos == 2:
            soma_coluna3 += matriz[linha][pos]

print('-=' * 30)
for linha in matriz:
    for pos in linha:
        print(f'[{pos:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')