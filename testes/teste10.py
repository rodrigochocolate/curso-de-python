cont = media = 0
maior = 0
menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    media += n
    cont += 1
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    if n < menor:
        menor = n
print(f'Você digitou {cont} números e a média foi {media / cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')