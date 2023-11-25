from datetime import date
maiores_de_idade = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Ano de nascimento da {c}ª Pessoa: '))
    idade = date.today().year - ano_nascimento
    if idade >= 21:
        maiores_de_idade += 1
print(f'Dessas 7 pessoas {maiores_de_idade} são maiores de idade!')
