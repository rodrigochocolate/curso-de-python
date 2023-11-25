homens = mais18 = mulheres_20 = 0
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
    if sexo == 'M':
        homens += 1
    if idade > 18:
        mais18 += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1
    if continuar == 'N':
        break
print(f'''====== FIM DO PROGRAMA ======
Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {homens} homens cadastrados
E temos {mulheres_20} mulheres com menos de 20 anos''')