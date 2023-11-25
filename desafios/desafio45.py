from random import randint
print('-' * 16)
print('JOGO DE JOKENPÔ')
print('-' * 16)
pc = randint(1, 3)
print('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
escolha = int(input('Escolha: '))

if escolha == 1 and pc == 3:
    print('O jogador escolheu PEDRA e PEDRA vence TESOURA!')
elif escolha == 2 and pc == 1:
    print('O jogador escolheu PAPEL e PAPEL vence PEDRA!')
elif escolha == 3 and pc == 2:
    print('O jogador escolheu TESOURA e TESOURA vence PAPEL!')
elif pc == 1 and escolha == 3:
    print('O computador escolheu PEDRA e PEDRA vence TESOURA!')
elif pc == 2 and escolha == 1:
    print('O computador escolheu PAPEL e PAPEL vence PEDRA!')
elif pc == 3 and escolha == 2:
    print('O computador escolheu TESOURA e TESOURA vence PAPEL')
elif pc == escolha:
    print('O jogo empatou!')