n = int(input('Digite um número inteiro: '))
vezes = 0
for c in range(1, n + 1):
    if n % c == 0:
        vezes += 1
if vezes == 2:
    print('O número é primo!')
else:
    print('O número não é primo!')
