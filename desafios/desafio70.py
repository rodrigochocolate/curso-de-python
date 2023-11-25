totgasto = maisdemil = cont = 0
print('-' * 40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
while True:
    nome = str(input('Nome do produto: ')).title().strip()
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    totgasto += preco
    if preco > 1000:
        maisdemil += 1
    cont += 1
    if cont == 1:
        nomebarato = nome
        precobarato = preco
    if preco < precobarato:
        precobarato = preco
        nomebarato = nome
    if continuar == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'''O total da compra foi R${totgasto:.2f}
Temos {maisdemil} produtos custando mais de R$1000.00
O produto mais barato foi {nomebarato} que custa R${precobarato:.2f}''')
