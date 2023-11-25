from datetime import date

ano_atual = date.today().year
info = {'nome': str(input('Nome: ')).title(),
        'idade': ano_atual - int(input('Ano de nascimento: ')),
        'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if info['ctps'] != 0:
    contratacao = int(input('Ano de contratação: '))
    info['contratação'] = contratacao
    info['salario'] = float(input('Salário: R$ '))
    info['aposentadoria'] = info['contratação'] - (ano_atual - info["idade"]) + 35
print('-=' * 30)
print(info)
for k, v in info.items():
    print(f'{k} tem o valor {v}')