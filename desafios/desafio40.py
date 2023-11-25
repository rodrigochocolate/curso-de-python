n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é de {media:.2f}')
if media < 5:
    print('Você foi REPROVADO!')
elif 6.9 > media >= 5:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')
