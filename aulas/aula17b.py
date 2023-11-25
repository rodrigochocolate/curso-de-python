valores = list()
valores.append(int(input('Digite um valor: ')))
valores.append(int(input('Digite outro valor: ')))
valores.append(int(input('Digite o último valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')