from time import sleep


def manual(func):
    frase = func
    while func.upper() != 'FIM':
        print('\033[m\033[30;42m~' * 27)
        print('  SISTEMA DE AJUDA PyHELP  ')
        print('~' * 27)
        func = input(f'\033[m{frase}')
        sleep(0.25)
        if func.upper() != 'FIM':
            vezes = len(func) + 36
            print('\033[30;44m~' * vezes)
            print(f"  Acessando o manual do comando '{func}'  ")
            print('\033[30;44m~' * vezes)
            sleep(0.5)
            print('\033[m\033[7;30m', end='')
            help(func)
        sleep(1)
    print('\033[30;41m~' * 12)
    print('  ATÉ LOGO!  ')
    print('~' * 12)

    return func


# Programa Principal
funcao = manual('Função ou Biblioteca > ')
