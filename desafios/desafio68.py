from random import randint
vitorias = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('=-' * 15)
    n = int(input('Diga um valor: '))
    comp = randint(0, 10)
    p_i = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    tot = n + comp
    print('-' * 30)
    print(f'Você jogou {n} e o computador {comp}. Total de {tot} DEU ', end='')
    if tot % 2 == 0:
        deu = 'PAR'
    else:
        deu = 'ÍMPAR'
    print(deu)
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