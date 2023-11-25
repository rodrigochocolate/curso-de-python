from time import sleep


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sleep(0.5)
escolha = 0
maior = f'O maior número é o {n1}'
while escolha != 5:
    print('''\n----------------------
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
----------------------''')
    sleep(0.25)
    escolha = int(input('Qual é sua escolha? '))
    sleep(1)
    print()
    if escolha == 1:
        print(f'{n1} + {n2} é igual a {n1 + n2}')
    elif escolha == 2:
        print(f'{n1} x {n2} é igual a {n1 * n2}')
    elif escolha == 3:
        if n2 > n1:
            maior = f'O maior número é o {n2}'
        elif n1 == n2:
            maior = 'Os dois valores são iguais'
        print(maior)
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        escolha = 5
    sleep(1.5)

print(f'{" FIM ":=^30}')
