alunoinf = dict()
alunoinf['Nome'] = str(input('Nome: ')).strip().title()
alunoinf['Media'] = float(input(f'Média de {alunoinf["Nome"]}: '))
for k, inf in alunoinf.items():
    print(f'{k} é igual a {inf}')
print('Situação é igual a Aprovado' if alunoinf['Media'] >= 7 else 'Situação é igual a Reprovado')
