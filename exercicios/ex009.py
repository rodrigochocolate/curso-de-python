n1 = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{n1} x {c:02} = {n1 * c}')
print('-' * 12)