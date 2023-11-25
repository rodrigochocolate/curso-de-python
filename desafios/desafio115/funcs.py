def menu():
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('-' * 40)


def cadastros():
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    with open('cadastros.txt', 'r') as arquivo:
        pos = 0
        for cadastro in arquivo:
            if pos % 2 == 0:
                print(cadastro)
            else:
                print(cadastro, end='')


def novo_cadastro():
    print('-' * 40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' * 40)
    with open('cadastros.txt', 'a') as arquivo:
        nome = str(input('Nome: ')).title()
        while True:
            try:
                idade = int(input('Idade: '))
                break
            except:
                print('\033[31mERRO: Digite um número inteiro válido\033[m')
        cadastro = [nome, idade]
        for inf in cadastro:
            if inf == cadastro[0]:
                arquivo.write(inf + '\t\t\t')
            else:
                arquivo.write(f'{inf} anos' + '\n')
    print(f'Novo registro de {nome} adicionado.')
