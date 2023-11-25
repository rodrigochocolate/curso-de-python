from random import randint
from time import sleep
print('\033[1;35mGERANDO um NÚMERO ENTRE 0 e 5...')
sleep(3)
c = randint(0, 5)
p = int(input('\033[0;34mTente adivinhar: '))

if p == c:
    print('\033[1;32mParabéns!\033[0;32m Você acertou!')
else:
    print(f'\033[1;31mVocê errou!\033[0;31m O número era \033[1;32m{c}\033[0;31m!')