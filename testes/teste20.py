locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whadon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]
c = 1
for e in locadora:
    print(f'--- {c}º FILME ---')
    for k, v in e.items():
        print(f'O {k} é {v}')
    c += 1