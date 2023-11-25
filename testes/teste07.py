print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
termos = 10
u = razao * 9 + primeiro
mostrados = 0
while termos != 0:
    if cont <= termos:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
        mostrados += 1
    if cont == termos + 1:
        print('PAUSA')
        termos = int(input('Quantos termos você quer mostrar a mais? '))
        primeiro = u + razao
        cont = 1
print(f'Progressão finalizada com {mostrados} termos mostrados.')
