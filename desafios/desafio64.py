n = s = 0
c = -1
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número (999 para parar): '))
print(f'A soma entre os {c} valores digitado é {s}')
