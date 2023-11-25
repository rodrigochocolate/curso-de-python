from random import randint
from time import sleep

n1 = int(input('Primeiro número: '))
sleep(0.5)
n2 = int(input('Segundo número: '))
soma = n1 + n2
lista = [n1, n2]
sleep(1.5)
print(f'\n{max(lista)} + {min(lista)} é igual a {soma}')
sleep(2)
print('\nAgora é minha vez de escolher os números e a sua de somar!')
sleep(3)
print('\nESCOLHENDO OS NÚMEROS...')
sleep(2)
p1 = randint(1, 100)
p2 = randint(1, 100)
lista02 = [p1, p2]
soma02 = p1 + p2
sleep(0.5)
print('\nNúmeros gerados!')
resposta = int(input(f'\n{max(lista02)} + {min(lista02)} é igual a '))
if resposta == soma02:
    print('\033[1;32mParabéns, você acertou!')
else:
    print(f'\033[31mVocê errou! A soma era \033[1;31m{soma02}')