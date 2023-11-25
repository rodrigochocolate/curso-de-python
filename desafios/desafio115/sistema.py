from desafios.desafio115 import funcs
from time import sleep

while True:
    funcs.menu()
    while True:
        try:
            opcao = int(input('Sua opção: '))
        except:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            if opcao in [1, 2, 3]:
                break
            else:
                print('ERRO! Digite um opção válida!')
    if opcao == 1:
        funcs.cadastros()
    elif opcao == 2:
        funcs.novo_cadastro()
    elif opcao == 3:
        print('-' * 40)
        print(f'{"Saindo do sistema... Até logo!":^40}')
        print('-' * 40)
        break
    sleep(2)
