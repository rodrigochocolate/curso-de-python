#No lugar de procurar a posição do chapecoense eu coloquei o flamengo, já que o chapecoense não está mais na lista

from time import sleep
times = 'São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthias', 'Ceará SC', 'Atlético-GO', 'Bragantino', 'Forteleza', 'Sport Recife', 'Bahia', 'Vasco da Gama', 'Goiás', 'Botafogo', 'Coritiba'
while True:
    print('''\033[34m[ 1 ] Lista de times do brasileirão
[ 2 ] Os 5 primeiros times
[ 3 ] Os 4 últimos times
[ 4 ] Lista dos times em ordem alfabética
[ 5 ] Posição do Flamengo
[ 6 ] Sair do programa\033[34m''')
    print('\033[1;33m=' * 30, '\033[m')
    opcao = int(input('\033[32mQual é sua opção? '))
    sleep(0.5)
    if opcao == 1:
        print(f'\n\033[34mLista de times do Brasileirão: ')
        for time in times:
            print(f'\033[30m{time}')
    elif opcao == 2:
        print(f'\n\033[34mOs 5 primeiros times são: ')
        for time in range(0, 5):
            print(f'\033[30m{times[time]}')
            sleep(0.25)
    elif opcao == 3:
        print(f'\n\033[34mOs 4 últimos times são: ')
        for time in range(len(times) - 4, len(times)):
            print(f'\033[30m{times[time]}')
            sleep(0.25)
    elif opcao == 4:
        print(f'\n\033[34mTimes em ordem alfabética: ')
        times_ordem = sorted(times)
        for time in times_ordem:
            print(f'\033[30m{time}')
    elif opcao == 5:
        print(f'\n\033[34mO Flamengo está na {times.index("Flamengo") + 1}ª posição ')
    elif opcao == 6:
        print('\033[1;35mFINALIZANDO...')
        sleep(2)
        break
    else:
        print('\033[31mOpção inválida. Tente novamente.')
        sleep(1)
    sleep(1)
    print('\033[1;33m=' * 30, '\033[m')