'''matriz = [[], [], []]
x = y = cont = 0
while True:
    n = int(input(f'Digite um valor para [{x}, {y}]: '))
    matriz[x].insert(y, n)
    y += 1
    if y == 3:
        y = 0
        x += 1
    cont += 1
    if cont == 9:
        break
print('-=' * 30)
for lin in matriz:
    for pos in lin:
        print(f'[{pos:^5}]', end='')
    print()'''

# Solução minha 17/1/2021
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        n = int(input(f'Digite um valor para a posição [{x}, {y}]: '))
        matriz[x][y] = n
for lin in matriz:
    for num in lin:
        print(f'[{num:^5}]', end=' ')
    print()