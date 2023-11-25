nome = str(input('Digite seu nome completo: ')).title().strip().split()
print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nome[0]}
Seu último nome é {nome[-1]}''')
