salario = float(input('Qual é o salário do funcionário? R$'))
salario_novo = salario * 15 / 100 + salario
if salario > 1250:
    salario_novo = salario * 10 / 100 + salario
print(f'Quem ganhava R${salario:.2f} passou a ganhar R${salario_novo:.2f} agora.')
