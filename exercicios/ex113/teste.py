'''from exercicios.ex113.funcs import leiaInt, leiaFloat

numInt = leiaInt('Digite um Inteiro: ')
numFloat = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}')'''
# Solução do Curso em Vídeo
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor intero digitado foi {n1} e o real foi {n2}')