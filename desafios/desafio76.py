produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2
            , 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
for pos, produto in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{produto:.<30}', end='')
    else:
        print(f'R${produto:>7.2f}')
print('-' * 40)