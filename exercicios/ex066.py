soma = valores = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    valores += 1
print(f'A soma dos {valores} valores foi {soma}!')
