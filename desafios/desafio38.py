n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n2 > n1:
    maior = n2
    print('O segundo valor é o maior')
    print('O primeiro valor é o menor')
elif n2 == n1:
    print('Os dois valores são iguais')
elif n1 > n2:
    print('O primeiro valor é o maior')
    print('O segundo valor é o menor')
