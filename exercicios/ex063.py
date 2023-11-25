print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
termos = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
cont = 3
print('~' * 30)
print(f'{t1} -> {t2}', end=' -> ')
while cont <= termos:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~' * 30)
