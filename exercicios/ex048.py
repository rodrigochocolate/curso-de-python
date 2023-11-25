soma = cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitado é {soma}')