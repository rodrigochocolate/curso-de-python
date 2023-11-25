'''matriz = [[], [], []]
for x in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Digite um valor para [{x}, {y}]: '))
        matriz[x].insert(y, n)
print('-=' * 30)
for lin in matriz:
    for num in lin:
        print(f'[{num:^5}] ', end='')
    print()'''

# Solução do Curso em Vídeo
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):       # For de alimentação
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):        # Estruturas para mostrar a estrutura
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()