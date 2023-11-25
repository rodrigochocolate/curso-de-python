from datetime import date


def voto(ano):
    global idade
    idade = date.today().year - ano
    if 65 >= idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    else:
        if idade < 16:
            return 'NÃO VOTA'
        else:
            return 'VOTO OPCIONAL'


print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
lei = voto(nascimento)
print(f'Com {idade} anos: {lei}.')
