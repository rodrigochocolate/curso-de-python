from random import randint
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    print('-=' * 15)
    jogador = int(input('Digite um valor: '))
    p_i = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    while p_i not in 'PI':
        p_i = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    comp = randint(0, 10)
    tot = jogador + comp
    if tot % 2 == 0:
        deu = 'PAR'
    else:
        deu = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {comp}. Total de {tot} DEU {deu}')
    print('-' * 30)
    if deu == 'PAR' and p_i == 'P' or deu == 'ÍMPAR' and p_i == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')
