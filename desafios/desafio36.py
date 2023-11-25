casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos vai pagar? '))
salario_30 = salario * 30 / 100
prestacao = casa / (anos * 12)
if prestacao > salario_30:
    print('O empréstimo foi negado!')
elif prestacao <= salario_30:
    print(f'A prestação mensal vai ser de R${prestacao:.2f}')
