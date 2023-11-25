from random import randint
sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in sorteados:
    print(n, end=' ')
#print(f'\nO maior valor sorteado foi {sorted(sorteados)[-1]}')
#print(f'O menor valor sorteado foi {sorted(sorteados)[0]}')
print(f'\nO maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')