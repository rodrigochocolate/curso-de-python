print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + razao * 9
termo = primeiro
while termo <= decimo:
    print(termo, end=' -> ')
    termo += razao
print('ACABOU!')
