lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for pos, n in enumerate(lista):
    if n == max(lista):
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for pos, n in enumerate(lista):
    if n == min(lista):
        print(pos, end='... ')
print()