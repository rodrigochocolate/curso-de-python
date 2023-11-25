from random import sample
lista = []
for c in range(1, 5):
    a = str(input(f'{c}º Aluno: ')).title()
    lista.append(a)
ordem = sample(lista, 4)
print(ordem)
