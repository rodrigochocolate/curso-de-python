a = [2, 3, 4, 7]
b = a           # Faz uma ligação entre a lista A e B
b = a[:]        # Cria uma copiá
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')