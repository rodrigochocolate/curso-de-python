r = 'S'
lista = []
pesos = []
while r in 'Ss':
    inform = [str(input('Nome: ')).title(), float(input('Peso: '))]
    lista.append(inform[:])
    pesos.append(inform[1])
    inform.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
print(lista)
print(max(pesos))
print(min(pesos))
