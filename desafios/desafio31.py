distancia_viagem = float(input('Distância da viagem: (Km)'))
if distancia_viagem > 200:
    passagem = distancia_viagem * 0.45
else:
    passagem = distancia_viagem * 0.50
print(f'A passagem ira acustar R${passagem:.2f}')