continuar = 'S'
cont = media = maior = menor = 0
while continuar == 'S':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    continuar = str(input('Quer continuar [S/N]? ')).upper()[0]
    cont += 1
    media += n
print(f'\nA média dos valores lidos é de {media / cont}')
print(f'O maior valor lido foi {maior} e o menor foi {menor}')
