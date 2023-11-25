velocidade_carro = float(input('Velocidade do carro: '))
if velocidade_carro > 80:
    print(f'Você foi multado! A multa vai custar R${(velocidade_carro - 80) * 7:.2f}')