media_idade = 0
nome_velho = ''
idade_velho = 0
mulheres_menos_20 = 0
for c in range(1, 5):
    #print('-' * 12)
    c = f' {c}ª PESSOA '
    print(f'{c:-^30}')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    media_idade += idade
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
print('-' * 30)
print(f'\nA média de idade do grupo é de {media_idade / 4} anos')
print(f'O homem mais velho do grupo tem {idade_velho} anos e se chama {nome_velho}')
print(f'No grupo existe {mulheres_menos_20} mulheres com menos de 20 anos')