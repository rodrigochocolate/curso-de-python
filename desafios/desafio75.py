tupla = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
pares = 0
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
for num in tupla:
    if num % 2 == 0:
        pares += 1
        if pares == 1:
            print(f'Os valores pares digitados foram ', end='')
        print(num, end=' ')
    elif num == tupla[-1] and pares == 0:
        print(f'Nenhum valor par foi digitado')