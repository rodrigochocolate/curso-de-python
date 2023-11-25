n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
maior = n1
menor = n1
if n3 < n2 > n1:
    maior = n2
elif n2 < n3 > n1:
    maior = n3
elif n3 > n2 < n1:
    menor = n2
elif n2 > n3 < n1:
    menor = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')