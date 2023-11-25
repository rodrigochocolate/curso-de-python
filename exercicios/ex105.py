#def notas(*nts, sit=False):
#    """
#    -> Função para analisar notas e situações de vários alunos.
#    :param nts: uma ou mais notas dos alunos (aceita várias).
#    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
#    :return: dicionário com várias informações sobre a situação da turma.
#    """
#    tot = len(nts)
#    soma = sum(nts)
#    media = soma / len(nts)
#    info = {'total': tot, 'maior': max(nts),
#            'menor': min(nts), 'média': media}
#    if sit:
#        if media < 5:
#            info['situação'] = 'RUIM'
#        elif media < 7:
#            info['situação'] = 'RAZOÁVEL'
#        else:
#            info['situação'] = 'BOA'
#    return info


#resp = notas(5.5, 9.5, 4, 6.5, sit=False)
#help(notas)

# Solução do Curso em Vídeo
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, sit=True)
print(resp)
help(notas)