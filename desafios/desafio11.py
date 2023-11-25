lar = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = lar * alt
litros = area / 2
print(f'Para pintar {area:.1f}m² você precisa de {litros:.1f}l')