maior = menor = 0
for c in range(1, 6):
    peso = float(input('Peso: (Kg) '))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi {maior}Kg e o menor peso lido foi {menor}Kg.')