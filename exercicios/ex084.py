'''r = 'S'
lista = []
pesos = []
cadastros = 0
while r in 'Ss':
    inform = [str(input('Nome: ')).title(), float(input('Peso: '))]
    lista.append(inform[:])
    pesos.append(inform[1])
    inform.clear()
    cadastros += 1
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
print('-=' * 30)
print(f'Ao todo, você cadastrou {cadastros} pessoas.')
print(f'O maior peso lido foi {max(pesos)}Kg. Peso de ', end='')
for p in lista:
    if p[1] == max(pesos):
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso lido foi {min(pesos)}Kg. Peso de ', end='')
for p in lista:
    if p[1] == min(pesos):
        print(f'[{p[0]}]', end=' ')
print()'''

# Solução do Curso em Vídeo
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()