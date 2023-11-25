def cab(msg):
    vezes = len(msg) + 4
    print('~' * vezes)
    print(f'{msg:^{vezes}}')
    print('~' * vezes)


cab('Gustavo Guanabara')

cab('Curso de Python no Youtube')

cab('CeV')