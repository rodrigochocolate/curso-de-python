from time import sleep
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
tupla = 1, 1, 1, 1, 1
print('GERANDO 5 NÚMEROS ENTRE 0 E 10', end='')
for ponto in range(1, 4):
    sleep(0.67)
    print('.', end='')
print('\n\nNÚMEROS GERADOS!')
for pos, num in enumerate(tupla):
    print(f'{pos + 1}º NÚMERO GERADO: {num:2}')
    sleep(0.25)
while True:
    print('''\n[ 1 ] Maior número
[ 2 ] Menor número
[ 3 ] Sair do programa''')
    opcao = int(input('Qual é sua opção? '))
    while str(opcao) not in '123':
        opcao = int(input('Opção Inválida. Qual é sua opção? '))
    if str(opcao) in '12':
        sleep(1)
    if opcao == 1 or opcao == 2:
        maior = sorted(tupla)[-1]
        menor = sorted(tupla)[0]
        if maior == menor:
            print('\nTodos os números são iguais!')
        elif opcao == 1:
            print(f'\nO Maior valor lido foi {maior}')
        elif opcao == 2:
            print(f'\nO Menor valor lido foi {menor}')
    if opcao == 3:
        print('\nFINALIZANDO', end='')
        for ponto in range(1, 4):
            sleep(0.67)
            print('.', end='')
        break
    sleep(1)