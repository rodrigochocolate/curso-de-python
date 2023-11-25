frase = str(input('Digite um frase: ')).upper()
frase = frase.split()
frase = ''.join(frase)
count = frase.count("A")
primeira = frase.find("A") + 1
ultima = frase.rfind("A") + 1
if count == 0:
    print('A letra "A" não aparece nenhuma vez!')
else:
    print(f'A letra "A" aparece {count} vezes')
    print(f'A letra "A" aparece pela primeira vez na posição {primeira}')
    print(f'A letra "A" aparece pela ultima vez na posição {ultima}')
