primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ultimo = primeiro + razao * 9
termos = -1
mostrados = 0
while termos != 0:
    for c in range(primeiro, ultimo + 1, razao):
        print(c, end=' -> ')
        mostrados += 1
    print('ACABOU')
    termos = int(input('Quantos termos a mais? '))
    primeiro = c + razao
    ultimo = c + (razao * termos - 1) + razao
print(f'Ao todo foram mostrados {mostrados} termos!')