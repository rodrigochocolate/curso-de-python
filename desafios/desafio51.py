p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
u = p1 + (r * 9)
for c in range(p1, u + 1, r):
    print(c, end=' -> ')
print('ACABOU!')