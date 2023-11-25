from random import sample
lista = []
for a in range(1, 5):
    a1 = str(input(f'{a}º Aluno: '))
    lista.append(a1)

ordem = sample(lista, 4)
print(ordem)