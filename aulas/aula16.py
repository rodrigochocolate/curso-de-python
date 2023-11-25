#          0000000000    1111    22222    33333
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Bata Frita')
#         -4444444444   -3333   -22222   -11111

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):    # Usando o enumerate tem que dar o dado e o contador
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
