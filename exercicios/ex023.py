n1 = int(input('Informe um número: '))
print(f'Analisando o número {n1}')
print(f'''Unidade: {n1 // 1 % 10}
Dezena: {n1 // 10 % 10}
Centena: {n1 // 100 % 10}
Milhar: {n1 // 1000 % 10}''')
