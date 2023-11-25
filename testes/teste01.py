usuario = senha = ''
while usuario == senha:
    usuario = str(input('Usuário: ')).strip().title()
    senha = str(input('Senha: ')).strip().title()
    if usuario == senha:
        print('\nERRO! Sua SENHA é igual a seu USUÁRIO!\n')
print('\nUsuário e Senha CONCEDIDOS!')
