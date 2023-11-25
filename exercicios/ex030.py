n = int(input('\033[35mMe diga um número qualquer: '))
if n % 2 == 0:
    print(f'\033[mO número {n} é \033[1;34mPAR')
else:
    print(f'\033[mO número {n} é \033[1;34mÍMPAR')
