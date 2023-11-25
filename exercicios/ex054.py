from datetime import date
maiores = menores = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = date.today().year - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'Ao todo tivemos {menores} pessoas menores de idade')
