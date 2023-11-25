velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[1;31mMULTADO!\033[0;31m Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de \033[33mR${(velocidade - 80) * 7:.2f}!\033[m')
print('\033[32mTenha um bom dia! Dirija com segurança!')