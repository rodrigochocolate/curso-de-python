primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ultimo = primeiro + razao * 9
termo = c = 0
while c != 10:
    print(termo, end=' -> ')
    termo += razao
    c += 1
print('ACABOU!')