lista = []
mulheres = []
while True:
    info = dict()
    info['nome'] = str(input('Nome: ')).title()
    info['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    while info['sexo'] not in 'MF':
        info['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
    if info['sexo'] in 'F':
        mulheres.append(info['nome'])
    info['idade'] = int(input('Idade: '))
    lista.append(info.copy())
    resp = str(input('Quer continuar? [S/N] '))[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] '))[0]
    if resp in 'Nn':
        break
media = 0
for p in lista:
    media += p['idade']
pessoas = len(lista)
media = media / pessoas
print('-=' * 30)
print(f'- O grupo tem {pessoas} pessoas.')
print(f'- A média de idade é de {media}')
print(f'- As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m, end=' ')
print()
print(f'- Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] > media:
        print(f'\nnome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')
print(f'<< ENCERRANDO >>')