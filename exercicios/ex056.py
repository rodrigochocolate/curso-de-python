media_idade = 0
nome_velho = ''
idade_velho = 0
mulheres_menos20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media_idade += idade
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1
print('-' * 21)
print(f'A média de idade do grupo é de {media_idade / 4} anos')
print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres_menos20} mulheres com menos de 20 anos')