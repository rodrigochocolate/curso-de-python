cont = 0
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
    cont += 1
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
