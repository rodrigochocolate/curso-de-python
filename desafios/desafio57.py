sexo = 'J'
while sexo not in 'MF':
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    if sexo not in 'MF':
        print('Sexo inválido! Informe o valor correto.')
print('Sexo validado!')
