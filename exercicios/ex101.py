'''from datetime import date
def voto():
    print('-' * 30)
    nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nasc
    if idade < 18:
        lei = 'NÃO VOTA'
    elif idade >= 70:
        lei = 'VOTO OPCIONAL'
    else:
        lei = 'VOTO OBRIGATÓRIO'
    print(f'Com {idade} anos: {lei}.')


voto()'''

# Solução do Curso em Vídeo


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))