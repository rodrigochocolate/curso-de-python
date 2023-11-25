def notas(* notas, sit=False):
    """
    -> Função para analisar notas e situções de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    total = soma = 0
    for nota in notas:
        total += 1
        soma += nota
    info = {'total': total, 'maior': max(notas),
            'menor': min(notas), 'média': soma / len(notas)}
    if sit == True:
        if info['média'] >= 7:
            info['situação'] = 'BOA'
        elif info['média'] >= 6:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['média'] = 'RUIM'
    return info


# Programa Principal
resp = notas(7.5, 5.5, 5, 6.5, 2, 10, 9.5, 7, sit=True)
print(resp)
help(notas)