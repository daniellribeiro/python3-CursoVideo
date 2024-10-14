def notas(notas,sit=False):
    """
    Funcao para analisar notas e situacoes de varios alunos
    :param notas:
    :param sit:
    :return:
    """
    r = dict()
    r['numeroNotas'] = len(notas)
    r['maiorNota'] = max(notas)
    r['menorNota'] = min(notas)
    r['media'] = round(sum(notas) / len(notas),1)
    if sit:
        if r['media'] > 6:
            r['situacao'] = 'SITUACAO BOA'
        else:
            r['situacao'] = 'SITUACAO RUIM'
    return r

print(notas([5.5,2.5,1.5,1,2,2.578],sit=True))
#help(notas)