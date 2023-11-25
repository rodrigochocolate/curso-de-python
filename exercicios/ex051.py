print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
u = r * 9 + p1
for c in range(p1, u + 1, r):
    print(c, end=' -> ')
print('ACABOU')