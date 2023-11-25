def leiaInt(num):
    print('-' * 30)
    frase = num
    while num not in '-1-2-3-4-5-6-7-8-9' or num == '':
        num = input(frase)
        if num not in '-1-2-3-4-5-6-7-8-9' or num == '':
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')