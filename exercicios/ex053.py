frase = str(input('Digite um frase: ')).upper().strip().split()
frase = ''.join(frase)
frase_invertida = frase[::-1]
print(f'O inverso de {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
