n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = n1
while True:
    print('''Escolha uma opção:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('Qual opção? '))
    print('~' * 35)
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} multiplicado por {n2} é igual a {n1 * n2}')
    elif opcao == 3:
        if n2 > n1:
            maior = n2
        elif n1 == n2:
            maior = 0
            print(f'Não tem valor maior, os dois são iguais!')
        if maior != 0:
            print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        maior = n1
    elif opcao == 5:
        break
    else:
        print('Opção inválida. Tente novamente!')
print('FIM DO PROGRAMA...')