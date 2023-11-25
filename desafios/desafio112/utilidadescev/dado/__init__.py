def leiaDinheiro(msg):
    ok = False
    while True:
        n = str(input(msg))
        n2 = n
        if n.count(',') == 1:
            n2 = n.replace(',', '')
        elif n.count('.') == 1:
            n2 = n.replace('.', '')
        c1 = c2 = 0
        for l in n2:
            if l in '1234567890-':
                c1 += 1
            else:
                c2 += 1
        if c2 == 0 < c1 and n2.count('-') <= 1:
            if n2.count('-') == 1 and n2[0] == '-' or n2.count('-') == 0:
                ok = True
        if ok:
            if ',' in n:
                n = n.replace(',', '.')
            if '.' in n:
                n = float(n)
            else:
                n = int(n)
            break
        else:
            print(f'\033[31mERRO! "{n}" é um preço inválido!\033[m')
    return n
