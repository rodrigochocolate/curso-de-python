'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')'''
nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}')
