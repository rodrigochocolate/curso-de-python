from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    computador = randint(0, 10)
    print('-=' * 15)
    jogador = int(input('Digite um valor: '))
    total = computador + jogador
    p_i = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    print('-' * 30)
    if total % 2 == 0:
        deu = 'PAR'
    elif total % 2 != 0:
        deu = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {deu}')
    print('-' * 30)
    if deu == 'PAR' and p_i == 'P' or deu == 'ÍMPAR' and p_i == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
print('-=' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')