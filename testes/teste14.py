print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)
total = mais_1000 = preco_barato = 0
nome_produto = ''
cont = 0
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    while preco < 0:
        preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preco
    if preco > 1000:
        mais_1000 += 1
    if cont == 0:
        preco_barato = preco
    if preco < preco_barato:
        preco_barato = preco
        nome_produto = nome
    cont += 1
    if continuar == 'N':
        break
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {mais_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto} que custa R${preco_barato:.2f}')
