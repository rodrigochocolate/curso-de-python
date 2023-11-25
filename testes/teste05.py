from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção inválida. Tente novamente')
    sleep(1.5)
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')
