from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {nascimento + 18}')
elif idade > 18:
    print(f'Você ja deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {nascimento + 18}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
