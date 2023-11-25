peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / altura ** 2
print(f'O seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO de PESO!')
elif 25 > imc >= 18.5:
    print('Você está com o PESO IDEAL!')
elif 30 > imc >= 25:
    print('Você está SOBREPESO!')
elif 40 > imc >= 30:
    print('Você está OBESO!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')