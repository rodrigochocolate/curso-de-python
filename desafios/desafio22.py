nome = str(input('Nome completo: '))
print(nome.upper())
print(nome.lower())
letras = len(nome) - nome.count(' ')
print(f'O nome {nome.title()} tem {letras} caracteres')
print(f'O primeiro nome tem {len((nome.split())[0])} caracteres')