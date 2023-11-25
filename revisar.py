from random import randint
from time import sleep

print(f'\033[33m{"-" * 12}\033[1mREVISOR DE DESAFIOS!\033[0;33m{"-" * 12}')
a = int(input('\n\033[32mVocê quer sortear do desafio '))
sleep(0.25)
b = int(input('Até o '))
sleep(0.5)
print('\n\033[1;35mSORTEANDO DESAFIO', end='')
c = randint(a, b)
for d in range(1, 4):
    sleep(0.67)
    print('\033[0;35m.', end='')
sleep(0.25)
print(f'\n\n\033[34mVocê deve revisar o desafio ', end='')
sleep(0.33)
print(f'\033[1;34m{c // 100 % 10}', end='')
sleep(0.33)
print(f'{c // 10 % 10}', end='')
sleep(0.33)
print(f'{c // 1 % 10}', end='')
sleep(0.50)
