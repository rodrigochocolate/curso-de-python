try:
    n = int(input('\033[33mInforme um valor: '))
except ValueError:
    print('\033[1;31mERRO!\033[0;31m Você deve digitar um valor inteiro.')