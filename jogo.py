def lin(vezes, carc='-'):
    print(carc * vezes)


def cab(txt):
    lin(30, '~')
    print(f'{txt:^30}')
    lin(30, '~')


def menu():
    print(f'{" MENU ":-^30}')
    print('[ 1 ] Par')
    print('[ 2 ] Ímpar')
    lin(30)


cab('Jogo de Par ou Ímpar')
menu()
opcao = -1
c = 0
while c != 2:
    j = ['Primeiro', 'Segundo']
    try:
        j[c] = int(input(f'{j[c]} jogador: '))
    except (ValueError, TypeError):
        print(f'\033[31mERRO! Digite um número inteiro.\033[m')
    else:
        if j[c] in [1, 2]:
            c += 1
        else:
            print(f'\033[31mERRO! \'{j[c]}\' não está dentro do menu.\033[m')
cab('ESCOLHA DOS NÚMEROS')
