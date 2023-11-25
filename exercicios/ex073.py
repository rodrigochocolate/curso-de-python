times = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional',
         'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians',
         'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Fortaleza',
         'Sport recife', 'Bahia', 'Vasco da Gama', 'Goiás', 'Botafogo', 'Coritiba')

print('-=' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 40)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 40)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 40)
print(f'O Flamengo está na {times.index("Flamengo") + 1}ª posição')