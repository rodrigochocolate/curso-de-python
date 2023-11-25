frase = str(input('Digite um frase: ')).strip().upper().split()
frase = ''.join(frase)
frase_invertida = frase[::-1]
print(f'A inverso da frase {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('E por isso a frase digita é um PALÍNDROMO!')
else:
    print('E por isso a frase digita não é um PALÍNDROMO!')
