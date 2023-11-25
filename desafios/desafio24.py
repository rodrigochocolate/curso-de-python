cidade = str(input('Nome da cidade: ')).title().split()
print('Tem "Santo" no primeiro nome!' if 'Santo' in cidade[0] else 'Não tem "Santo" no primeiro nome!')
