compras = []
def carrega_continuar():
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    return
while True:
    produto = str(input('Nome do produto: ')).title().strip()
    compras.append(produto)
    carrega_continuar()
    while carrega_continuar() not in 'SN':
        carrega_continuar()
    if carrega_continuar() == 'N':
        break
print('Foram citados os seguintes produtos: ')
for p in range(0, len(compras)):
    if len(compras) - 1 != p != len(compras) - 2:
        print(compras[p], end=', ')
    else:
        if p == len(compras) - 2:
            print(compras[p], end=' e ')
        else:
            print(compras[p])
