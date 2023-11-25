maiores_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    print('-' * 25)
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('-' * 25)
    idade = int(input('Idade: '))
    while idade > 150:
        idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 25)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    if continuar == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^29}')
print(f'Total de pessoas com mais de 18 anos: {maiores_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos')
