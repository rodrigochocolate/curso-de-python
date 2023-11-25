n = int(input('Digite um número: '))
d = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}', end=' ')
        d += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número 10 foi divisível {d} vezes')
if d == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')