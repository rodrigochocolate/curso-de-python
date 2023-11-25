print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor / 50 >= 1:
        for c in range(50, valor + 1, 50):
            cedulas_50 += 1
        valor = valor - (cedulas_50 * 50)
        print(f'Total de {cedulas_50} cédulas de R$50')
    if valor / 20 >= 1:
        for c in range(20, valor + 1, 20):
            cedulas_20 += 1
        valor = valor - (cedulas_20 * 20)
        print(f'Total de {cedulas_20} cédulas de R$20')
    if valor / 10 >= 1:
        for c in range(10, valor + 1, 10):
            cedulas_10 += 1
        valor = valor - (cedulas_10 * 10)
        print(f'Total de {cedulas_10} cédulas de R$10')
    if valor / 1 >= 1:
        for c in range(1, valor + 1, 1):
            cedulas_1 += 1
        valor = valor - (cedulas_1 * 1)
        print(f'Total de {cedulas_1} cédulas de R$1')
    if valor == 0:
        break
print('=' * 30)
print('VOLTE SEMPRE AO BANCO CEV! Tenha um bom dia!')
