from time import sleep


def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    for v in valores:
        if maior == 0 or v > maior:
            maior = v
        print(v, end=' ')
        sleep(0.25)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()