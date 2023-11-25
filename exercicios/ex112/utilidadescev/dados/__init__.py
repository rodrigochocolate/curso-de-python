'''def leiaDinheiro(msg):
    while True:
        n1 = str(input(msg)).strip()
        n2 = n1
        if ',' in n1:
            n1 = n1.replace(',', '.')
        if '.' in n1:
            n2 = n1[:n1.index('.')]
        if n2.isnumeric() and n1.count('.') <= 1:
            if '.' in n1:
                n1 = float(n1)
            else:
                n1 = int(n1)
            return n1
        else:
            print(f'\033[31mERRO: "{n1}" é um preço inválido!\033[m')'''
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido\033[m')
        else:
            válido = True
            return float(entrada)