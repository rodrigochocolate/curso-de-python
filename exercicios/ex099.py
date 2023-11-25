'''from time import sleep


def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    for v in valores:
        print(v, end=' ')
        sleep(0.25)
        if valores[0] == v or v > maior:
            maior = v
    print(f'Foram informados {len(valores)} passados ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()'''

# Solução do Curso em Vídeo


from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()