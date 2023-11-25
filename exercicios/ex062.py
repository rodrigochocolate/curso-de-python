primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termos = 10
cont = 0
while termos != 0:
    ultimo = primeiro + razao * (termos - 1)
    for c in range(primeiro, ultimo + razao, razao):
        print(c, end=' -> ')
        cont += 1
        if c == ultimo:
            break
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    primeiro = ultimo + razao
print(f'Progressão finalizada com {cont} termos mostrados.')
