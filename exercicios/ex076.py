produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
            'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3,
            'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c, p in enumerate(produtos):
    if c % 2 == 0:
        print(f'{p:.<30}', end='')
    else:
        print(f'R${p:>7.2f}')
print('\033[1;4m~' * 40)
