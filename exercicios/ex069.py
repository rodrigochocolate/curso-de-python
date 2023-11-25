mais18 = homens = mulheres20 = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
