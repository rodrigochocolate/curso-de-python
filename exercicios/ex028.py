from time import sleep
from random import randint

print('\033[33m-=-' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-' * 20)
numero_secreto = randint(0, 5)
chute = int(input('\033[mEm que número pensei? '))
print('\033[35mPROCESSANDO', end='')
for c in range(1, 4):
    sleep(0.5)
    print('.', end='')
sleep(0.5)
if numero_secreto == chute:
    print('\n\033[1;32mPARABÉNS!\033[0;32m Você conseguiu me vencer!')
else:
    print(f'\n\033[1;31mGANHEI!\033[0;31m Eu pensei no número {numero_secreto} e não no {chute}!')
