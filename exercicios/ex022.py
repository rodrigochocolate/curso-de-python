from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome', end='')
for c in range(1, 4):
    print('.', end='')
    sleep(0.5)
print(f'\n\nSeu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])}')
