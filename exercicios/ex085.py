'''nums = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(nums[0])}')
print(f'Os valores ímpares digitados foram: {sorted(nums[1])}')'''

# Solução do Curso em Vídeo
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')