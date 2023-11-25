from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f'Seu alistamento será daqui {18 - idade} anos e você deve se alistar em {ano_nascimento + 18}')
elif idade == 18:
    print(f'Seu alistamento é esse ano!')
else:
    print(f'O seu alistamento foi a {idade - 18} anos e foi no ano de {ano_nascimento + 18}')