sexo = str(input('Informe seu sexo: [M/F] '))[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()[0]
print(f'\nSexo {sexo} registrado com sucesso!')
