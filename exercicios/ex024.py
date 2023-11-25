cidade = str(input('Em que cidade você nasceu? ')).title().strip().split()
print('Tem "Santo" no primeiro nome!' if 'Santo' in cidade[0] else 'Não tem "Santo" no primeiro nome!')
