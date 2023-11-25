lista = []
abertos = fechados = 0
expr = str(input('Digite a expressão: '))
for letra in expr:
    if letra == '(':
        lista.append(letra)
        abertos += 1
    elif letra == ')' and '(' in lista:
        lista.remove('(')
    if letra == ')':
        fechados += 1
if len(lista) == 0 and abertos == fechados:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')