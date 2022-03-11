def notas(*n, situacao=False):
    """
    --> Função para analisar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos(aceita várias)
    :param situacao: valor adicional, indicando se deve ou não indicar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = float(f'{sum(n)/len(n):.1f}')
    if situacao:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma


# PROGRAMA PRINCIPAL
resp = notas(6, 4, 6, situacao=True)
print(resp)
