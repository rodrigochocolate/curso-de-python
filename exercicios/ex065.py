r = 'S'
soma = cont = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'''Você digitou {cont} números e a média foi {soma / cont}
O maior valor foi {maior} e o menor foi {menor}''')
