salario = float(input('Salário do funcionário: R$'))
if salario > 1250:
    novo_salario = salario + salario * 10 / 100
else:
    novo_salario = salario + salario * 15 / 100
print(f'O salário do funcionário que custava R${salario:.2f} passou a custar R${novo_salario:.2f}')
