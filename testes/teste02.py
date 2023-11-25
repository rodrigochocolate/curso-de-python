nome = 'aa'
idade = 151
salario = -1
sexo = 'e'
civil = 'j'
while len(nome) < 3:
    nome = str(input('Nome: ')).strip()
while idade > 150:
    idade = int(input('Idade: '))
while salario < 0:
    salario = float(input('Salário: '))
while sexo not in 'mf':
    sexo = str(input('Sexo: [M/F] ')).lower()
while civil not in 'scvd':
    civil = str(input('Estado civil: '))
