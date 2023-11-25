n = int(input('Informe um valor: '))
print('\033[1;34m------------')
for c in range(1, 11):
    print(f'\033[0;33m{n} \033[30mx \033[36m{c:2} \033[30m= \033[1;32m{n * c}\033[m')
print('\033[1;34m------------')
