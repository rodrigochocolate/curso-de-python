'''pessoas = list()
media = 0
while True:
    info = dict()
    info['nome'] = str(input('Nome: ')).title()
    info['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    while info['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        info['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    info['idade'] = int(input('Idade: '))
    media += info['idade']
    pessoas.append(info.copy())
    resp = str(input('Quer continuar? [S/N] '))[0].upper()
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] '))[0].upper()
    if resp == 'N':
        break
media = media / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    for s in p['sexo']:
        if p['sexo'] == 'F':
            print(p['nome'], end=' ')
print(f'\nD) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')'''

# Solução do Curso em Vídeo
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')