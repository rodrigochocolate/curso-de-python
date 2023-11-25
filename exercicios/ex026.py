frase = str(input('Digite um frase: ')).upper().strip()
print(f'''A letra A aparece {frase.count("A")} vezes na frase.
A primeira letra A apareceu na posição {frase.find("A") + 1}
A última letra A apareceu na posição {frase.rfind("A") + 1}''')