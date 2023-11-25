from random import randint

print('-=' * 15)
print(f'{"JOGO DE MATEMÁTICA":^30}')
print('-=' * 15)
while True:
    print('''--------------------
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
--------------------''')
    opcao = int(input('>>> Opção:   '))
    while opcao not in [1, 2, 3, 4]:
        print('Opção inválida. Tente novamente.')
        opcao = int(input('>>> Opção:   '))
    chances = int(input('>>> Chances: '))
    while chances <= 0:
        chances = int(input('>>> Chances: '))
    print('-' * 20)
    tentativas = 1
    nums = [randint(1, 100), randint(1, 100)]
    nums = [max(nums), min(nums)]
    resp = 0
    if opcao == 1:
        resu = sum(nums)
        opr = '+'
    elif opcao == 2:
        resu = nums[0] - nums[1]
        opr = '-'
    elif opcao == 3:
        resu = nums[0] * nums[1]
        opr = 'x'
    elif opcao == 4:
        resu = str(nums[0] / nums[1])
        resu = resu[:resu.index('.') + 3]
        resu = float(resu)
        opr = '/'
    while resp != resu and tentativas <= chances:
        print(f'{tentativas}º Tentativa.')
        resp = float(input(f'{nums[0]} {opr} {nums[1]} é '))
        print()
        if resp == resu:
            break
        tentativas += 1
    print('-' * 20)
    if resp == resu:
        print(f'PARABÉNS! Você ganhou com {tentativas} tentativa(s).')
    else:
        print('VOCÊ PERDEU! Suas chances acabaram :(')
    print('''--------------------
[ 1 ] Sair
[ 2 ] Continuar
--------------------''')
    escolha = int(input('>>> Opção:   '))
    while escolha not in [1, 2]:
        escolha = int(input('>>> Opção: '))
    if escolha == 1:
        break
    elif escolha == 2:
        continue
print('<< FIM >>')
