from random import choice
lista = []
for c in range(1, 5):
    a = str(input(f'{c}º Aluno: ')).title()
    lista.append(a)
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
