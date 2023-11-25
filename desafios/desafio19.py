from random import choice
lista = []
for a in range(1, 5):
    a1 = str(input(f'{a}º Aluno: '))
    lista.append(a1)
escolhido = choice(lista)
print(f'\nO aluno escolhido para apagar o quadro é {escolhido}')