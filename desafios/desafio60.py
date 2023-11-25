n = int(input('Digite um número: '))
cont = n
fact = 1
print(f'{n}! = ', end='')
while cont != 0:
    if cont == 1:
        print(cont, end=' = ')
    else:
        print(cont, end=' x ')
    fact *= cont
    cont -= 1
print(fact)
