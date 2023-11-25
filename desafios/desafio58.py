from random import randint
print('Vou pensar em número entre 0 e 10')
computador = randint(0, 10)
jogador = computador - 1
palpites = 0
while computador != jogador:
    jogador = int(input('Em que número eu pensei? '))
    if jogador > computador:
        print('Digite um número menor!')
    elif jogador < computador:
        print('Digite um número maior!')
    palpites += 1
print(f'Parabéns! Você precisou de {palpites} palpites para vencer.')
