nome = str(input('Qual é seu nome completo? ')).strip().title()
print('Tem "Silva" no nome!' if 'Silva' in nome else 'Não tem "Silva" no nome!')