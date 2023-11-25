'''from datetime import date
info = dict()
info['nome'] = str(input('Nome: ')).title()
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
info['idade'] = ano_atual - ano_nascimento
info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['ctps'] != 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['salário'] = float(input('Salário: R$'))
    info['aposentadoria'] = (info['contratação'] - ano_nascimento) + 35
print('-=' * 30)
for k, v in info.items():
    print(f'  - {k} tem o valor {v}')'''

# Solução do Curso em Vídeo
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')