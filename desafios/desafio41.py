from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos\n')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÂO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 20:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
